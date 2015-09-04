# GARI
Good Agent-based Romcom Intelligence

## Overview

Inspired by [NaNoGenMo](https://github.com/dariusk/NaNoGenMo-2014)

The goal is to generate a hopefully interesting fiction novel.

Our approach is to build goal-oriented agents with rich internal representations of their environment.

With this internal representation, characters will develop motivations and will interact in order to achieve goals.

With a bit of external control over some global parameters, a rom-com will be generated.

Also, agents will develop an internal representation of the world by crawling through the internet and learning from it.  Easy enough!

## Object model

- Environments have locations
- Locations contain objects and other agents
- Agents can travel to locations and act upon objects and other agents
- Agents have internal properties (emotions, state likee hunger...)
- Internal properties of agents can be affected by actions or by the passing of time (e.g. tiredness and hunger change over time even in a state of inaction)
- The goal of an agent is always to optimize some subset of its internal state
