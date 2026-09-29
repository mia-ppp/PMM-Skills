#!/usr/bin/env node
'use strict';

const fs = require('node:fs');
const path = require('node:path');

let pptxgen;
try {
  pptxgen = require('pptxgenjs');
} catch (error) {
  console.error('Missing dependency: install pptxgenjs where Node.js can resolve it.');
  process.exit(1);
}

const COLORS = {
  background: 'F7F4EE',
  brown: '34251F',
  text: '2D2723',
  muted: '766D66',
  copper: 'B86B45',
  copperLight: 'E9D5C8',
  rule: 'DDD5CC',
  white: 'FFFFFF',
};
const SW = 13.333;
const SH = 7.5;
const FONT = 'Aptos';

function fail(message) {
  console.error(message);
  process.exit(1);
}

function validateDeck(data) {
  if (!data || typeof data !== 'object') fail('Input must be a JSON object.');
  if (!data.company || typeof data.company !== 'string') fail('Input needs a company string.');
  if (!Number.isInteger(data.requiredMainSlides) || data.requiredMainSlides < 1) {
    fail('Input needs a positive requiredMainSlides integer from the approved outline.');
  }
  if (!Array.isArray(data.slides) || data.slides.length === 0) fail('Input needs a non-empty slides array.');
  for (const [index, slide] of data.slides.entries()) {
    const label = `Slide ${index + 1}`;
    if (!slide.eyebrow || !slide.headline || !slide.keyInsight) {
      fail(`${label} needs eyebrow, headline, and keyInsight fields.`);
    }
    if (!slide.eyebrow.endsWith(data.company)) {
      fail(`${label} eyebrow must end with the company name "${data.company}".`);
    }
    if (slide.type === 'table') {
      if (!Array.isArray(slide.columns) || !Array.isArray(slide.rows)) {
        fail(`${label} table needs columns and rows arrays.`);
      }
      if (slide.rows.some((row) => !Array.isArray(row) || row.length !== slide.columns.length)) {
        fail(`${label} has a table row whose cell count does not match its columns.`);
      }
    } else if (slide.type === 'steps') {
      if (!Array.isArray(slide.steps) || slide.steps.length !== 3) {
        fail(`${label} steps visual needs exactly three steps.`);
      }
    } else {
      fail(`${label} type must be "table" or "steps".`);
    }
    if (slide.appendix && !/^A\d+\b/.test(slide.eyebrow)) {
      fail(`${label} appendix eyebrow must start with an A-number, such as A1.`);
    }
  }
}

function addText(slide, text, options = {}) {
  slide.addText(String(text ?? ''), {
    fontFace: FONT,
    color: COLORS.text,
    margin: 0,
    breakLine: false,
    valign: 'mid',
    fit: 'shrink',
    ...options,
  });
}

function cellText(value) {
  if (typeof value === 'object' && value !== null) return value.text ?? '';
  return String(value ?? '');
}

function addTable(slide, spec, y, h) {
  const x = 0.72;
  const w = 11.9;
  const rows = spec.rows.length + 1;
  const colW = Array.isArray(spec.columnWidths) && spec.columnWidths.length === spec.columns.length
    ? spec.columnWidths
    : spec.columns.map(() => w / spec.columns.length);
  const tableRows = [spec.columns, ...spec.rows].map((row, rowIndex) => row.map((value, colIndex) => {
    const isHeader = rowIndex === 0;
    const isSelected = rowIndex > 0 && spec.highlightRow === rowIndex - 1;
    const fill = isHeader ? COLORS.brown : (isSelected ? COLORS.copperLight : COLORS.background);
    const color = isHeader ? COLORS.white : COLORS.text;
    return {
      text: cellText(value),
      options: {
        fill: { color: fill },
        color,
        bold: isHeader || isSelected,
        fontFace: FONT,
        fontSize: isHeader ? 12 : 11,
        margin: [0.10, 0.13, 0.10, 0.13],
        valign: 'mid',
        breakLine: false,
        border: { type: 'solid', color: COLORS.rule, pt: 0.6 },
        ...(colIndex === 0 && isSelected ? { color: COLORS.brown } : {}),
      },
    };
  }));
  slide.addTable(tableRows, {
    x, y, w, h,
    colW,
    rowH: h / rows,
    border: { type: 'solid', color: COLORS.rule, pt: 0.6 },
    margin: 0.1,
    fontFace: FONT,
    fontSize: 11,
    color: COLORS.text,
    valign: 'mid',
    autoFit: false,
    breakLine: false,
  });
}

function addSteps(slide, steps, y, h) {
  const gap = 0.20;
  const x0 = 0.72;
  const totalW = 11.9;
  const cardW = (totalW - gap * 2) / 3;
  steps.forEach((step, i) => {
    const x = x0 + i * (cardW + gap);
    slide.addShape(pptxgen.ShapeType.roundRect, {
      x, y, w: cardW, h,
      rectRadius: 0.08,
      fill: { color: i === 1 ? COLORS.copperLight : 'EFEAE2' },
      line: { color: COLORS.rule, width: 1 },
    });
    addText(slide, String(i + 1).padStart(2, '0'), {
      x: x + 0.24, y: y + 0.25, w: 0.48, h: 0.28,
      fontSize: 12, bold: true, color: COLORS.copper,
    });
    addText(slide, step.title, {
      x: x + 0.24, y: y + 0.75, w: cardW - 0.48, h: 0.55,
      fontSize: 19, bold: true, color: COLORS.brown,
    });
    addText(slide, step.body, {
      x: x + 0.24, y: y + 1.45, w: cardW - 0.48, h: h - 1.72,
      fontSize: 13, color: COLORS.text, valign: 'top',
    });
  });
}

function addDeckSlide(pptx, spec, index, count) {
  const slide = pptx.addSlide();
  slide.background = { color: COLORS.background };
  slide.addShape(pptxgen.ShapeType.rect, {
    x: 0, y: 0, w: SW, h: SH,
    line: { color: COLORS.background, transparency: 100 },
    fill: { color: COLORS.background },
  });

  addText(slide, spec.eyebrow, {
    x: 0.72, y: 0.38, w: 11.1, h: 0.25,
    fontSize: 10, bold: true, charSpacing: 1.4, color: COLORS.muted,
  });
  const hasSubline = Boolean(spec.subline);
  addText(slide, spec.headline, {
    x: 0.72, y: 0.78, w: 11.9, h: hasSubline ? 0.72 : 0.95,
    fontSize: 27, bold: true, color: COLORS.brown,
    valign: 'top', breakLine: false,
  });
  let contentY = hasSubline ? 1.66 : 1.88;
  if (hasSubline) {
    addText(slide, spec.subline, {
      x: 0.72, y: 1.48, w: 11.9, h: 0.34,
      fontSize: 13, color: COLORS.muted, valign: 'top',
    });
  }

  const contentH = 4.35 - (hasSubline ? 0.18 : 0);
  if (spec.type === 'table') addTable(slide, spec, contentY, contentH);
  if (spec.type === 'steps') addSteps(slide, spec.steps, contentY + 0.22, contentH - 0.45);

  slide.addShape(pptxgen.ShapeType.rect, {
    x: 0.72, y: 6.38, w: 11.9, h: 0.62,
    line: { color: COLORS.copperLight, transparency: 100 },
    fill: { color: COLORS.copperLight },
  });
  addText(slide, spec.keyInsight, {
    x: 0.96, y: 6.51, w: 11.3, h: 0.34,
    fontSize: 13, bold: true, color: COLORS.brown,
  });
  addText(slide, spec.appendix ? String(spec.eyebrow.match(/^A\d+/)?.[0] || `A${index + 1}`) : `${index + 1} / ${count}`, {
    x: 11.75, y: 7.12, w: 0.86, h: 0.18,
    fontSize: 9, color: COLORS.muted, align: 'right',
  });
  return slide;
}

async function main() {
  const [inputPath, outputPath] = process.argv.slice(2);
  if (!inputPath || !outputPath) {
    console.error('Usage: node build_deck.js <deck-data.json> <output.pptx>');
    process.exit(2);
  }
  let data;
  try {
    data = JSON.parse(fs.readFileSync(inputPath, 'utf8'));
  } catch (error) {
    fail(`Could not read valid JSON from ${inputPath}: ${error.message}`);
  }
  validateDeck(data);

  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_WIDE';
  pptx.author = 'Case Deck Builder';
  pptx.subject = `Take-home case deck for ${data.company}`;
  pptx.title = `${data.company} case deck`;
  pptx.company = data.company;
  pptx.lang = 'en-US';
  pptx.theme = {
    headFontFace: FONT,
    bodyFontFace: FONT,
    lang: 'en-US',
  };
  const mainSlides = data.slides.filter((slide) => !slide.appendix).length;
  const appendixSlides = data.slides.filter((slide) => slide.appendix).length;
  if (mainSlides !== data.requiredMainSlides) {
    fail(`Found ${mainSlides} main slides, but requiredMainSlides is ${data.requiredMainSlides}.`);
  }
  const appendixCap = Math.floor(mainSlides / 2);
  if (appendixSlides > appendixCap) {
    fail(`Appendix has ${appendixSlides} slides, above the cap of ${appendixCap} for ${mainSlides} main slides.`);
  }
  let mainIndex = 0;
  let appendixIndex = 0;
  data.slides.forEach((slide) => {
    const index = slide.appendix ? appendixIndex++ : mainIndex++;
    addDeckSlide(pptx, slide, index, mainSlides);
  });

  const resolvedOutput = path.resolve(outputPath);
  fs.mkdirSync(path.dirname(resolvedOutput), { recursive: true });
  await pptx.writeFile({ fileName: resolvedOutput });
  console.log(`Wrote ${resolvedOutput}`);
}

main().catch((error) => fail(error.message));
