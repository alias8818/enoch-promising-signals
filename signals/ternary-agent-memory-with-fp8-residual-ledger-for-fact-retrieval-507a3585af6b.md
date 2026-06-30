# Ternary Agent Memory with FP8 Residual Ledger for Fact Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-agent-memory-with-fp8-residual-ledger-for-fact-retrieval-507a3585af6b`
Run ID: `ternary-agent-memory-with-fp8-residual-ledger-for-fact-retrieval-507a3585af6b-20260523T025704940713+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8780efafda6d

## What looked useful

The residual ledger mechanism recovers ternary-only accuracy loss, but a full FP8 residual ledger is dominated by direct FP8 storage/accuracy in this bounded retrieval setting. Future work should only continue if the residual ledger is sparse, update-aware, or hardware-exploitable.

## Boundaries and scale limits

No natural-language agent memory traces, learned embedding distributions, online write/update workloads, compressed scoring kernels, or production hardware FP8 path were tested. Largest case was 20,000 facts x 256 dims with 2,000 queries.

## Claim scope

Synthetic vector fact-retrieval probe with exact dot-product scoring: ternary plus a full FP8 residual ledger recovers nearly all dense fp32 Recall@1 at about 3.15x fp32 compression, but is not practically superior to direct FP8, which matched or exceeded its recall in most cases at 4.0x fp32 compression.

## Why it stopped

Proxy/local synthetic test found a useful mechanism signal but an early practical falsification against the direct FP8 control; this is not a full real-agent validation.

## Recommended next action

Stop this full-residual design as no-paper evidence; run a budget-matched sparse residual follow-up only if testing a residual ledger that uses no more storage than direct FP8.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Budget-matched sparse FP8 residual ledger for fact retrieval
- Success threshold: At equal or lower bytes than direct FP8, sparse ternary+FP8 residual improves Recall@1 or MRR by at least 0.5 percentage points on hard retrieval settings, or shows a measured update/latency advantage with no accuracy loss.
- Stop condition: Stop if sparse residuals fail to beat direct FP8 at equal bytes on synthetic hard cases and at least one real embedding trace.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-agent-memory-with-fp8-residual-ledger-for-fact-retrieval-507a3585af6b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
