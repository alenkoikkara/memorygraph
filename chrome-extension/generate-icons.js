const sharp = require('sharp');
const fs = require('fs');

const svgBuffer = fs.readFileSync('./icons/icon.svg');

// Generate 16x16 icon
sharp(svgBuffer)
  .resize(16, 16)
  .png()
  .toFile('./icons/icon16.png')
  .catch(err => console.error('Error generating 16x16 icon:', err));

// Generate 48x48 icon
sharp(svgBuffer)
  .resize(48, 48)
  .png()
  .toFile('./icons/icon48.png')
  .catch(err => console.error('Error generating 48x48 icon:', err));

// Generate 128x128 icon
sharp(svgBuffer)
  .resize(128, 128)
  .png()
  .toFile('./icons/icon128.png')
  .catch(err => console.error('Error generating 128x128 icon:', err)); 