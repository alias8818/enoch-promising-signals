# Learned Residual Codebooks for 1.58-bit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-residual-codebooks-for-1-58-bit-8098ca950626`
Run ID: `learned-residual-codebooks-for-1-58-bit-8098ca950626-20260526T072340979044+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c5410934474a

## What looked useful

Residual block codebooks exploit structure in ternary quantization error: B64/K16 reduced weighted relative MSE by 10.81% at 1.6567 payload bits/weight and improved proxy perplexity from 195007 to 5250, but near-budget B256/K2 at 1.5935 bits/weight reduced reconstruction MSE by only 1.83%.

## Boundaries and scale limits

Tested only post-training quantization on distilgpt2 plus a tiny-gpt2 smoke. Perplexity proxy used 24 WikiText-2 snippets / 2453 tokens. No quantization-aware training, large model, packed kernel, full benchmark, or matched 2-bit baseline was run.

## Claim scope

On distilgpt2 transformer weight matrices, post-training learned residual vector codebooks reduce reconstruction error versus rowwise ternary quantization, and one above-budget residual setting improved a small perplexity proxy versus plain ternary. The run does not support a literal 1.58-bit paper claim.

## Why it stopped

No-paper useful signal: this was a bounded post-training/proxy probe, and the strongest result requires extra bits beyond 1.58 while near-budget gains are modest and reconstruction-only.

## Recommended next action

Run a bounded quantization-aware training follow-up on a GPT-2-small-class toy or small model with fully counted bit budgets near 1.58 and matched 2-bit/ternary controls; stop if near-budget residual codebooks do not improve validation perplexity by at least 5% over ternary at equal or lower payload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware residual codebooks at a fully counted 1.58-bit budget
- Success threshold: At <=1.60 counted payload bits/weight, residual codebooks reduce validation perplexity by at least 5% versus matched ternary and are competitive with or better than a matched 2-bit baseline on the same model/eval.
- Stop condition: Stop if <=1.60 counted payload bits/weight fails to improve validation perplexity by 5% over ternary, or if gains vanish when codebook/index overhead is fully counted.

## Evidence references

- Artifact root: `<local-path>/projects/learned-residual-codebooks-for-1-58-bit-8098ca950626`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
