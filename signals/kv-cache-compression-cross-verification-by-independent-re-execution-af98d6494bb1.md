# KV-cache Compression Cross-Verification by Independent Re-Execution

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-cross-verification-by-independent-re-execution-af98d6494bb1`
Run ID: `kv-cache-compression-cross-verification-by-independent-re-execution-af98d6494bb1-20260611T071338966475+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e509d1003508

## What looked useful

Independent re-execution found that recency-only KV-cache compression probes are insufficient: practical fixed policies had near-zero target retention and high relative output error on needle retrieval traces, while query-aware/oracle controls retained the target and matched full attention much better.

## Boundaries and scale limits

Synthetic single-query attention only; no full transformer, no real KV tensors, no multi-step generation, no end-to-end serving latency, and no learned compressor. Tested sequence lengths up to 4096, dimension 64, 20 seeds, and 12.5%/25% retention.

## Claim scope

A CPU-only NumPy re-execution of single-query attention on deterministic synthetic KV traces shows that fixed recent/sink/norm KV retention policies preserve recency-biased traces much better than older-token retrieval traces, while query-dot/oracle controls preserve the retrieval target by scoring all keys.

## Why it stopped

Closed as no-paper useful signal: the evidence is a synthetic mechanism cross-check, not a full validation or full falsification of production KV-cache compression.

## Recommended next action

Run a bounded deepen follow-up that extracts real KV tensors from a small open transformer on retrieval prompts and applies the same full-vs-compressed attention fidelity checks with selection cost charged.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV retrieval fidelity check for fixed versus query-aware cache compression
- Success threshold: At 12.5% or 25% retention, fixed policies have at least 2x higher relative attention-output error or at least 0.3 lower retained target attention mass than query-aware/oracle controls on retrieval prompts, while recency controls remain comparatively preserved.
- Stop condition: Stop if real KV extraction cannot run locally within a bounded CPU/GPU budget, or if fixed policies match query-aware controls within 10% error and target-mass difference across retrieval prompts.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-cross-verification-by-independent-re-execution-af98d6494bb1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
