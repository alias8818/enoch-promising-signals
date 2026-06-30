# Counterexample Mining Loop for Agent Self-Correction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-mining-loop-for-agent-self-correction-337f34e0d547`
Run ID: `counterexample-mining-loop-for-agent-self-correction-337f34e0d547-20260613T002002009909+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ce43259ae602

## What looked useful

Across 40 train/holdout splits, layered doctrine memory raised mean holdout accuracy from 0.831 to 0.996, corrected 32.80 additional baseline failures on average, and introduced 0.00 mean regressions. Exact transcript search did not improve held-out accuracy; flat retrieval corrected failures but caused many regressions.

## Boundaries and scale limits

The evidence is synthetic and proxy-only for real agents: no LLM was run, counterexample features were structured, candidate rules were predefined, and the benchmark did not include noisy traces or adversarial memory contamination.

## Claim scope

In a deterministic synthetic replay benchmark with 304 exception-rule tasks and predefined candidate predicates, consolidating mined counterexamples into layered doctrine rules improved held-out correction over no-memory and exact transcript search without observed regressions.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy evidence for the mechanism, not publication-grade validation on real agents.

## Recommended next action

Run a bounded deepen test on real repeated-agent traces or a small LLM agent where counterexamples must be mined from natural-language failures rather than oracle task features.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language counterexample mining on repeated-agent replay traces
- Success threshold: At least +10 percentage points held-out accuracy versus no-memory, at least 50% of baseline held-out failures corrected, and less than 5% regressions from baseline-correct cases across at least three replay families.
- Stop condition: Stop if natural-language mined memories fail to beat exact transcript search by 5 percentage points or cause regressions above 10% on baseline-correct held-out cases.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-mining-loop-for-agent-self-correction-337f34e0d547`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
