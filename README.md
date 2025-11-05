# yeet

> deploy your slop using AI inference

## what is this

`yeet` deploys your application using AI inference. That's it. That's the whole thing.

`yeet` has no arguments and works on the current directory.

The `yoten` command finds where it was yeeted and delivers the facts about where the slop was slapped and whether it is fire or not.

## installation

```bash
uv pip install yeet
```

or if you're old school:

```bash
pip install yeet
```

or if you're based:

```bash
uvx yeet
```

## usage

### yeet - deploy your slop

```bash
cd your-project
yeet
```

That's it. `yeet` will:
1. Analyze your project using Claude
2. Figure out what kind of slop you're shipping
3. Tell you exactly what commands to run to deploy it
4. Judge your tech stack (optional but guaranteed)
5. Save your deployment URL so you can check if it's fire later

### yoten - check if your slop is fire

```bash
yoten
```

`yoten` will:
1. Find where you yeeted your slop
2. Hit that URL
3. Determine if it's fire 🔥, mid, or cooked 💀
4. Roast you accordingly

## requirements

- Python 3.12+
- An Anthropic API key (set `ANTHROPIC_API_KEY` env var)
- The audacity to ship

## output examples

```
$ yeet
analyzing slop...
asking claude what this slop is...

╭─ Analysis Complete ─╮
│ Detected: Next.js    │
│ Platform: Vercel     │
│ Why: vercel literally│
│ made next.js bestie  │
╰──────────────────────╯

your tech stack is more bloated than a webpack bundle

Run these commands to yeet your slop:
  1. npm install -g vercel
  2. vercel --prod
  ...

$ yoten
╭─ yoten - check if your slop is fire ─╮

Your Next.js app was yeeted to Vercel 2 hours ago
URL: https://my-app.vercel.app

checking if it's fire...
your slop is fire 🔥 no cap
Status: 200 | Response time: 0.34s
```

## faq

**Q: Does this actually work?**
A: Surprisingly yes

**Q: Should I use this in production?**
A: That's between you and god

**Q: Why?**
A: Someone tweeted it and I made it real

**Q: What platforms does it support?**
A: Whatever Claude thinks is best. Usually Fly.io, Vercel, Railway, Render, Netlify, or your mom's basement

**Q: Can I configure it?**
A: No. Zero config. That's the whole vibe.

**Q: What if it's wrong?**
A: Then Claude was wrong and you should yell at Claude not me

**Q: My deployment failed**
A: Skill issue

## license

MIT or whatever. I literally don't care. Fork it. Ship it. Yeet it.

## contributing

PRs welcome if they're funny or actually useful. Preferably both.

## credits

- Inspired by [this tweet](https://x.com/SIP200OK/status/1985847424259178989)
- Powered by Claude (Anthropic)
- Built with `uv` because pip is for boomers
- Vibes: immaculate

---

*slop responsibly* 🫡
