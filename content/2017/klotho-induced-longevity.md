---
date: '2017-06-08'
title: Klotho induced longevity
category: English
tags: 23andMe, DNA, genetics, Python, SNP
---

It all started with a string of people telling me how I looked younger than my
age. Shaving my beard didn't help either.

Then a friend was mocking me on how childish I appears on some of my last
photos. And was jocking I might be affected by a mutation on *Klotho*-related
genes.

What the fuck is that? Turns out it really exist, and there's a SNP tied to
that hormone and called [rs9536314
](https://www.snpedia.com/index.php/Rs9536314).

Luckily, it is a SNP covered by the first generation of 23andMe chips. Having
downloaded the raw data a while back, it is a matter of installing the Python
[`arv`](https://github.com/cslarsen/arv) package:

```shell-session
$ pip install arv
Collecting arv
  Downloading arv-0.9.2-cp27-none-macosx_10_12_intel.whl (92kB)
    100% |████████████████████████████████| 102kB 10kB/s
Collecting cython>=0.25 (from arv)
  Downloading Cython-0.25.2-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (4.1MB)
    100% |████████████████████████████████| 4.1MB 201kB/s
Installing collected packages: cython, arv
Successfully installed arv-0.9.2 cython-0.25.2
```

Let's now find out about that SNP:

```pycon
>>> from arv import load
>>> genome = load("kev_full_genome.txt")
>>> genome["rs9536314"]
<SNP: chromosome=13 position=33628138 genotype=<Genotype 'GT'>>
>>>
```

Bingo! With the `GT` variant, I'm supposed to have higher plasma klotho
concentration. Which is, [according to some studies
](https://www.snpedia.com/index.php/Rs9536314), reported to:

- affect longevity in mice,
- associated with greater brain cortical volume,
- show lower less decline with age on standardized cognitive tests,
- score better on some Alzheimer's disease tests.

As usual all these studies are preliminary and should be taken with a huge
grain of salt.

But my friend's diagnostic was right. My dear friend, you made my day and I owe
you a mojito! ;)

And thanks Mom and Dad for your DNA! :)
