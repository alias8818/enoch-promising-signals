# Top-k Gradient Sparsification for 2-Node Home GPT-2 Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `top-k-gradient-sparsification-for-2-node-home-gpt-2-training-5de1a3b517d1`
Run ID: `top-k-gradient-sparsification-for-2-node-home-gpt-2-training-5de1a3b517d1-20260603T224343919579+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/50e283a1c954

## What looked useful

Dense reached mean final eval loss 0.3603 across two seeds. Top-k+EF reached 0.4282 at 5% and 0.3907 at 10%, with 90.0% and 80.0% payload reductions respectively. Top-k+EF at 1% reached 0.6991, showing a clear convergence tradeoff despite 98.0% payload reduction.

## Boundaries and scale limits

No real two-node Ethernet training was run; communication was modeled from payload bytes. No GPT-2-small-scale model, real token corpus, long-run optimizer stability, mixed-precision compression, network overlap, NCCL/Gloo collective, or multi-hour validation was tested.

## Claim scope

In a two-simulated-worker, single-GB10 tiny GPT-style training proxy with 0.93M parameters and synthetic held-out sequence data, top-k gradient sparsification with error feedback at 5-10% preserved most dense-baseline convergence while reducing modeled gradient payload by 80-90%. A 1% setting reduced payload by 98% but lagged dense convergence substantially.

## Why it stopped

Proxy-only evidence supports the mechanism but does not directly validate actual 2-node home GPT-2 training or provide publication-grade results.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete action is a bounded real two-node Ethernet validation using dense, 5% top-k+EF, and 10% top-k+EF on a GPT-2-small-class or parameter-matched GPT workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real 2-node Ethernet validation of 5-10% top-k error-feedback GPT training
- Success threshold: Top-k+EF achieves at least 20% higher wall-clock tokens/sec than dense while final validation loss is within 10% of dense at matched tokens for 5% or 10% sparsity.
- Stop condition: Stop if 5% and 10% top-k+EF are both slower than dense after communication overhead is included, or if both exceed dense final validation loss by more than 10% at matched tokens.

## Evidence references

- Artifact root: `<local-path>/projects/top-k-gradient-sparsification-for-2-node-home-gpt-2-training-5de1a3b517d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
