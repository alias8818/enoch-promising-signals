# Full WikiText-2 GPT-2 small int4 residual adapter rank and training-depth confirmation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `full-wikitext-2-gpt-2-small-int4-residual-adapter-rank-and-c8efdce170`
Run ID: `full-wikitext-2-gpt-2-small-int4-residual-adapter-rank-and-c8efdce170-20260605T123506356355+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: GPT-2-small-class 4-bit proxy residual adapter validation: enoch://control-plane/projects/gpt-2-small-class-4-bit-proxy-residual-adapter-validation-6695d7121b/runs/gpt-2-small-class-4-bit-proxy-residual-adapter-validation-6695d7121b-20260605T035001305558+0000
- Parent run decision: Real-int4 GPT-2 small residual adapter versus matched adapter baselines: enoch://control-plane/projects/real-int4-gpt-2-small-residual-adapter-versus-matched-adap-dbf14811b5/runs/real-int4-gpt-2-small-residual-adapter-versus-matched-adap-dbf14811b5-20260605T074014319953+0000

## What looked useful

Frozen simulated int4 GPT-2 small scored 57.514 validation PPL versus 44.409 for unquantized GPT-2. Best completed adapter run was rank 8 depth 4 at LR 2e-6 with PPL 56.244, a small 2.21% PPL reduction and only about 8.6% recovery of the int4-vs-FP loss gap. Rank scaling was non-monotonic: rank 4 depth 2 beat rank 8 and rank 16 depth 2 at the stable LR.

## Boundaries and scale limits

Single GB10 worker; one fixed seed for completed main runs; WikiText-2 only; simulated int4 dequantized weights rather than vendor int4 kernels; depth 6 and 12 training attempts were SIGTERM-limited; no multi-seed robustness or baseline against other adapter/quantization methods.

## Claim scope

On GPT-2 small with full WikiText-2 validation and simulated groupwise int4 projection weights, FP32 residual low-rank adapters on the top 2-4 blocks can produce a small validation perplexity recovery after one epoch, but the recovery is fragile and far from restoring unquantized GPT-2 quality.

## Why it stopped

Bounded direct validation found only a small, fragile adapter recovery and no robust rank/depth confirmation; deeper training configurations were execution-limited rather than validating a stronger claim.

## Recommended next action

Stop paper pursuit for this run; the useful next bounded action is to fix the depth>=6 SIGTERM path and rerun rank 4/8 depth 4/6 with validation-selected early stopping across 3 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed early-stopped GPT-2 small int4 residual adapter depth-4/depth-6 confirmation
- Success threshold: Mean best-validation PPL improves at least 3% over frozen int4 with no seed worse than frozen int4, and the improvement closes at least 15% of the int4-vs-FP validation loss gap.
- Stop condition: Stop if depth>=6 still SIGTERMs after one harness/resource fix, or if two seeds fail to beat frozen int4 by at least 1% best-validation PPL.

## Evidence references

- Artifact root: `<local-path>/projects/full-wikitext-2-gpt-2-small-int4-residual-adapter-rank-and-c8efdce170`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
