# Natural-corpus Tiny GPT-2-class domain grid

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-corpus-tiny-gpt-2-class-domain-grid-028a02b5b2`
Run ID: `natural-corpus-tiny-gpt-2-class-domain-grid-028a02b5b2-20260628T231748309336+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Domain Proportion Grid for Tiny GPT-2 Pretraining: enoch://control-plane/projects/domain-proportion-grid-for-tiny-gpt-2-pretraining-91e64b5f947d/runs/domain-proportion-grid-for-tiny-gpt-2-pretraining-91e64b5f947d-20260628T214941813519+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4581481eb0d4

## What looked useful

The 300-step run produced mean own-vs-other gap 0.0822 nats/byte and mean pooled-minus-specialized own-domain gap 0.0940 nats/byte, but only 1/4 domain-specialized models ranked their own held-out domain lowest. The stronger clean-domain-grid hypothesis is not supported under this bounded setup.

## Boundaries and scale limits

Byte-level tokenizer proxy, four domains, one seed, 300 steps/model, CPU-only local run, 122k parameters; not GPT-2-small scale and not publication-grade robustness.

## Claim scope

On four 20 Newsgroups domains, a 122,624-parameter byte-level GPT-style causal Transformer trained for 300 CPU steps per domain showed a small average own-domain loss advantage over a pooled control, but did not produce a clean own-domain cross-entropy ranking grid.

## Why it stopped

Bounded local evidence is mixed and fails the stricter own-domain rank criterion, so this is an early proxy falsification rather than a full validation.

## Recommended next action

Stop this run as no-paper useful signal; if pursued, run a bounded deepen test with GPT-2 BPE/tokenization, matched compute budgets, and multiple seeds before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched BPE Tiny GPT domain-grid confirmation
- Success threshold: At least 3/4 own-domain rank hits in the mean grid, positive mean own-vs-other gap, and specialized own-domain loss no worse than pooled on at least 3/4 domains across seeds.
- Stop condition: Stop if mean own-domain rank hits remain below 3/4 or if pooled control matches/beats specialized models on at least half of own-domain comparisons.

## Evidence references

- Artifact root: `<local-path>/projects/natural-corpus-tiny-gpt-2-class-domain-grid-028a02b5b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
