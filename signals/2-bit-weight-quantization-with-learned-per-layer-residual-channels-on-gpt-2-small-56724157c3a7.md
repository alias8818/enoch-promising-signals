# 2-bit weight quantization with learned per-layer residual channels on GPT-2-small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `2-bit-weight-quantization-with-learned-per-layer-residual-channels-on-gpt-2-small-56724157c3a7`
Run ID: `2-bit-weight-quantization-with-learned-per-layer-residual-channels-on-gpt-2-small-56724157c3a7-20260621T075402235644+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/114ecde8251c

## What looked useful

Learned residual channels reduced mean validation loss from 36.5505 for 2-bit projections to 8.7383, outperforming magnitude residual channel selection at 14.3273 under the same 5.03% active-channel budget, but remained far above fp32 loss of 3.8922.

## Boundaries and scale limits

Only 8 calibration batches and 8 evaluation batches per run at sequence length 128 were tested, with three seeds. The implementation does not use packed 2-bit kernels, does not evaluate full-corpus perplexity, does not test model sizes beyond GPT-2-small, and does not sweep residual budgets.

## Claim scope

On a bounded GPT-2-small Wikitext-2 validation probe, learned per-module residual channel gates at a fixed 5.03% active-channel budget recover more causal language-model loss than random or residual-norm magnitude residual-channel controls for 2-bit-equivalent projection weight quantization.

## Why it stopped

No-paper useful signal: direct local evidence supports the mechanism, but the run is too small and the learned residual model remains too far from fp32 to justify a paper-positive decision.

## Recommended next action

Run a bounded deepen follow-up with a residual-budget sweep and larger held-out token count to test whether the learned-over-magnitude advantage persists before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Budget sweep for learned residual channels in 2-bit GPT-2-small quantization
- Success threshold: Learned residual channels beat magnitude residual channels by at least 0.5 validation loss at two or more residual budgets while closing at least 80% of the 2-bit-to-fp32 loss gap at one budget.
- Stop condition: Stop if learned channels fail to beat magnitude channels by at least 0.2 validation loss at 5% and 10% budgets, or if larger-token evaluation eliminates the learned-over-magnitude advantage.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-weight-quantization-with-learned-per-layer-residual-channels-on-gpt-2-small-56724157c3a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
