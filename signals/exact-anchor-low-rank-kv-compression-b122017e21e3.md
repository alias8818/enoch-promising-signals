# Exact-Anchor Low-Rank KV Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-low-rank-kv-compression-b122017e21e3`
Run ID: `exact-anchor-low-rank-kv-compression-b122017e21e3-20260526T060220937972+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2df4cd4f2a67

## What looked useful

Exact anchors are not free: at rank 2/4/8/16 with 12.5% anchors, exact-anchor mean relative MSE was 0.6754/0.5441/0.4376/0.2794, while budget-matched global low-rank achieved 0.5491/0.4993/0.4070/0.2668. Equal-rank comparisons looked positive, so storage-budget matching is essential for this idea.

## Boundaries and scale limits

Tested only attention-output reconstruction, not logits, perplexity, serving latency, compression overhead, long contexts, GPT-2-small-class full evaluation, or larger LLMs.

## Claim scope

On a local DistilGPT-2 attention-output reconstruction probe over 24 layer/head tensors at sequence length 192, heuristic exact-anchor low-rank KV compression improves error at equal residual rank but loses to a global low-rank baseline matched for approximate float storage budget.

## Why it stopped

Early direct attention-output evidence falsifies the practical storage-efficiency claim for the tested heuristic; this is not a full validation of all possible anchor methods.

## Recommended next action

Stop this heuristic exact-anchor variant as no-paper evidence; a bounded follow-up should test budget-aware or learned anchor selection against budget-matched global low-rank on logits/perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Budget-aware anchor selection for low-rank KV compression
- Success threshold: At equal approximate KV storage, exact-anchor compression must reduce mean logits KL or perplexity degradation by at least 10% versus global low-rank while not increasing estimated decode-step overhead by more than 5%.
- Stop condition: Stop if budget-aware anchors fail to beat budget-matched global low-rank on both logits KL and perplexity delta across two anchor budgets.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-low-rank-kv-compression-b122017e21e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
