# CompressedState: Retrieval-Free Compressed Memory Recall

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressedstate-retrieval-free-compressed-memory-recall-6e1af3f62388`
Run ID: `compressedstate-retrieval-free-compressed-memory-recall-6e1af3f62388-20260621T070912182303+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/37227f7a15f9

## What looked useful

Compressed-state recall can be accurate for small/low-load memories, e.g. n=128,d=64,no-noise reached 0.961 at 4x compression and key_dim=512,n=512,d=512,no-noise reached 0.995 at 8x compression. The same mechanism degraded sharply at larger loads: key_dim=128,n=2048,d=1024,no-noise reached only 0.337, and n=8192,d=1024 only 0.102, while exact lookup stayed at 1.000.

## Boundaries and scale limits

Runs were short synthetic probes, not language-model integration or full retrieval benchmarks. Accuracy collapsed at higher item counts, query noise, or low effective feature rank; no 7B-scale or long-context training was attempted.

## Claim scope

Synthetic random-vector key/value associative recall with exact lookup baseline and fixed compressed-state superposition on GB10 CUDA. Evidence supports a low-load compressed-state mechanism but not broad retrieval-free memory replacement.

## Why it stopped

Moderate synthetic evidence shows a capacity-limited mechanism but early-falsifies the broad retrieval-free compressed-memory recall claim as a drop-in retrieval replacement; this is proxy evidence, not full validation.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should evaluate learned or key-orthogonalized compressed states against ANN retrieval on noisy synthetic semantic recall.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Orthogonalized Compressed States for Noisy Semantic Recall
- Success threshold: Compressed-state method achieves >=0.9 recall at >=4x memory compression for n >= 2048 and query noise >=0.05, without worse query latency than ANN baseline.
- Stop condition: Stop if recall remains below 0.8 at n=2048 with >=4x compression after learned/orthogonalized encoding, or if latency/memory advantages vanish at the accuracy threshold.

## Evidence references

- Artifact root: `<local-path>/projects/compressedstate-retrieval-free-compressed-memory-recall-6e1af3f62388`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
