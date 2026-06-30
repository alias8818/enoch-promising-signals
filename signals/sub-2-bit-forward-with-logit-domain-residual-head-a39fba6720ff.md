# Sub-2-bit forward with logit-domain residual head

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sub-2-bit-forward-with-logit-domain-residual-head-a39fba6720ff`
Run ID: `sub-2-bit-forward-with-logit-domain-residual-head-a39fba6720ff-20260620T003115813632+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b77064485f94

## What looked useful

The mechanism is worth a bounded standard-corpus follow-up: logit-domain residual correction recovered a stable majority of local held-out quantization damage, but corrected CE remained far worse than dense GPT-2 and same-domain CE showed overfitting risk.

## Boundaries and scale limits

Evidence is limited to GPT-2-small, tiny local repeated training text, a distinct local held-out text proxy, three seeds, adapter-only training, and no optimized sub-2-bit inference kernels or standard benchmark corpus.

## Claim scope

On a GPT-2-small local proxy, a rank-16 logit-domain residual head equal to 0.656% of teacher parameters consistently recovered about 57% of the held-out CE gap and reduced teacher KL by about 57% after ternarizing unique matrix weights to 1.386 empirical bits/weight.

## Why it stopped

No-paper useful signal: local proxy evidence supports the mechanism, but it is not direct standard-corpus or publication-grade validation.

## Recommended next action

Run a bounded standard-corpus GPT-2-small deepening probe on WikiText-2 or C4 shards with the same ternary forward, residual-head ranks 4/8/16/32, and held-out CE/KL plus inference-memory accounting before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard-corpus GPT-2-small residual-head recovery after sub-2-bit ternary quantization
- Success threshold: Mean held-out CE-gap recovery >= 50% and KL-to-teacher reduction >= 50% for a residual head <= 1% of teacher parameters, without same-domain-only overfitting.
- Stop condition: Stop as negative if all tested ranks <= 1% of teacher parameters recover < 25% of the held-out CE gap or reduce KL-to-teacher by < 25%.

## Evidence references

- Artifact root: `<local-path>/projects/sub-2-bit-forward-with-logit-domain-residual-head-a39fba6720ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
