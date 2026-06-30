# Real-transformer packed-memory validation for tier-adaptive quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-transformer-packed-memory-validation-for-tier-adaptiv-c431f20569`
Run ID: `real-transformer-packed-memory-validation-for-tier-adaptiv-c431f20569-20260614T054702497534+0000`

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

- Parent run decision: Tier-Adaptive Quantization Cascade on GB10 VRAM Budget: enoch://control-plane/projects/tier-adaptive-quantization-cascade-on-gb10-vram-budget-71d535402e5e/runs/tier-adaptive-quantization-cascade-on-gb10-vram-budget-71d535402e5e-20260614T050501837279+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/353f49aa9e91

## What looked useful

The best adaptive setting reduced packed projection/lm-head storage by 52.08% and had only 0.0058 nats eval loss delta, beating uniform 4-bit loss degradation, but top-1 agreement was 0.6992 versus the 0.95 threshold. Uniform 8-bit reached 0.0414 nats loss delta and 0.8943 top-1 agreement. All completed runs passed packed-code round-trip checks for 25 modules.

## Boundaries and scale limits

Single pretrained distilgpt2 model, 16 local prompt strings, inference-only CUDA evaluation, dequantized forward pass after validating packed integer-code round trips; no custom packed matmul kernel, no training, no GPT-2-small-class or larger validation.

## Claim scope

On distilgpt2 with row-wise symmetric packed 4/8-bit quantization of Linear/Conv1D projection and lm_head weights, sensitivity-ranked tiering can preserve eval loss at a 75% high-bit module fraction while reducing packed fp16 weight storage by about 52%, but it does not preserve next-token top-1 agreement.

## Why it stopped

Bounded direct Tier 1 validation produced useful no-paper evidence: storage and loss behavior were promising, but the simple module-level tier-adaptive method failed the token-stability threshold and is not paper-positive.

## Recommended next action

Run a bounded deepen test with activation-aware row/group tiering and an explicit lm_head policy, keeping the same packed-byte accounting and requiring top-1 agreement improvement before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware row/group tiering for packed transformer quantization
- Success threshold: At least 40% packed storage reduction versus fp16, eval loss delta no more than 0.05 nats, masked-token top-1 agreement at least 0.90, and better loss/top-1 behavior than uniform 4-bit.
- Stop condition: Stop if activation-aware tiering cannot exceed 0.80 top-1 agreement while maintaining at least 40% packed storage reduction, or if its loss delta exceeds uniform 8-bit by more than 0.05 nats.

## Evidence references

- Artifact root: `<local-path>/projects/real-transformer-packed-memory-validation-for-tier-adaptiv-c431f20569`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
