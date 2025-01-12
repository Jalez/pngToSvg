<!-- @format -->

# 🎨 PNG to SVG Converter

Convert your boring PNGs into exciting SVGs with this way-too-overcomplicated Docker solution! Because who doesn't love using a container to run a single command? 🐳

## 🚀 Prerequisites

- Docker (because running a simple script natively is too mainstream)
- Some PNG files (preferably not blank ones, but hey, we won't judge)
- Basic will to live (optional but recommended)

## 🎯 Quick Start

1. Clone this repo (or download it, we're not your boss)
2. Place your PNG file in the same directory and name it `image.png` (yes, we're very creative)
3. Make the scripts executable (if you're on Unix/Linux/Mac):

```bash
chmod +x convert.sh check_deps.sh
```

4. Run the converter:

```bash
./convert.sh
```

5. Marvel at your new `output.svg` file (results may vary, no refunds)

## 🔍 Checking Dependencies

Feel paranoid about whether everything is installed correctly? We got you covered!

```bash
./check_deps.sh
```

## 🤔 Why Docker?

Because:

- It's 2025 and everything needs to be containerized
- We love spending 500MB of disk space to run a 10KB script
- Someone probably mentioned it in a job interview

## 📝 Notes

- Only converts one file at a time (we believe in quality over quantity)
- Needs to be named `image.png` (we're not good with choices)
- Creates `output.svg` (again, creativity peaked at naming things)

## 🐛 Troubleshooting

1. Nothing works?

   - Have you tried turning Docker off and on again?
   - Are you sure you're not trying to convert a JPEG named `image.png`?

2. The SVG looks weird?
   - That's not a bug, it's a feature
   - Try squinting, it might help

## 📜 License

Feel free to use this overengineered solution however you want. We're not responsible for:

- Excessive disk usage
- Questioning your life choices
- Explaining to your boss why you're using Docker for this

## 🙏 Contributing

Found a way to make this even more complicated? PRs welcome!

## 🌟 Star History

No stars yet. We're not surprised. 😅
