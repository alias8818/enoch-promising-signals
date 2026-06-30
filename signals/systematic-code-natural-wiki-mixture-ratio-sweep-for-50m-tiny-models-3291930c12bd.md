# Systematic Code-Natural-Wiki Mixture Ratio Sweep for 50M Tiny Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `systematic-code-natural-wiki-mixture-ratio-sweep-for-50m-tiny-models-3291930c12bd`
Run ID: `systematic-code-natural-wiki-mixture-ratio-sweep-for-50m-tiny-models-3291930c12bd-20260612T212511940998+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2961e3a1fc9d

## What looked useful

The sweep gives a reproducible caution and next-test target: low wiki allocation (10%) caused a large wiki loss penalty, each 60% domain-heavy mix overfit/specialized toward its target domain, and the balanced ratio was best for aggregate and worst-domain robustness in this proxy.

## Boundaries and scale limits

Not a paper-ready 50M corpus result: generated proxy corpus only, byte-level tokenizer, 491,520 byte tokens per model, 120 optimizer steps per ratio, five grid points, one seed, no real public code/natural/wiki datasets, and no convergence-scale training.

## Claim scope

In a one-seed controlled proxy using generated code-shaped, natural-prose-shaped, and wiki-shaped text, a 48.17M-parameter byte-level causal Transformer showed strong mixture-ratio specialization: domain-heavy mixtures minimized their own held-out domain loss, while the balanced 1/3-1/3-1/3 mixture minimized both mean validation loss and worst-domain validation loss across the five tested ratios.

## Why it stopped

No-paper useful signal only: the result is a controlled proxy and early mixture-ratio screen, not direct/full validation on real code, natural text, and Wikipedia corpora.

## Recommended next action

Run a bounded deepen follow-up on real mini-corpora with the same 48M-class model, fixed tokenizer, three seeds, and the same five ratios; stop if the balanced-vs-domain-heavy tradeoff or the low-wiki penalty does not reproduce.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Mini-Corpus Replication of 50M Code-Natural-Wiki Ratio Tradeoffs
- Success threshold: Balanced ratio has the best or statistically tied best mean and worst-domain loss across seeds, while each domain-heavy ratio retains its own-domain loss advantage and worsens at least one non-target domain.
- Stop condition: Stop as a negative or inconclusive deepen result if the balanced aggregate advantage or low-wiki penalty disappears across three seeds on real corpora.

## Evidence references

- Artifact root: `<local-path>/projects/systematic-code-natural-wiki-mixture-ratio-sweep-for-50m-tiny-models-3291930c12bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
