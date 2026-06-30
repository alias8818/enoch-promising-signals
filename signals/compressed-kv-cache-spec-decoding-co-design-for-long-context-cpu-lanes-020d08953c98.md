# Compressed-KV cache + spec decoding co-design for long-context CPU lanes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-kv-cache-spec-decoding-co-design-for-long-context-cpu-lanes-020d08953c98`
Run ID: `compressed-kv-cache-spec-decoding-co-design-for-long-context-cpu-lanes-020d08953c98-20260621T044654565229+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8fbf2e47f7f9

## What looked useful

Compressed KV reduced proxy KV bytes to 0.277-0.449 of fp32 with max relative L2 attention-output error 0.0069, but the compressed verifier was slower in every case: measured speedup 0.130x-0.590x, median 0.383x. A simple speculative model with draft cost ratio 0.2 never exceeded 0.674x end-to-end speedup.

## Boundaries and scale limits

Not a full language-model serving result; does not test fused int8 kernels, production attention backends, 7B+ model dimensions, real draft/target acceptance distributions, NUMA pinning, or multi-threaded CPU serving.

## Claim scope

Bounded CPU/NumPy proxy for row-wise int8 compression of old KV entries plus fp32 recent window during speculative-style verification batches at contexts 1024-16384 and dim 64.

## Why it stopped

Proxy early falsification: the directly tested naive compressed-KV speculative verifier saved memory and preserved approximate attention outputs, but was slower than full KV in every measured CPU case.

## Recommended next action

Stop this naive path as no-paper evidence; if continuing, implement a fused/blockwise int8 verifier that avoids materializing dequantized old KV and compare it against the same full-precision baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused int8 old-KV verifier for speculative CPU batches
- Success threshold: At context >= 8192 and q_batch >= 4, compressed verifier speedup >= 1.15x versus full fp32 while maintaining relative L2 error < 0.01.
- Stop condition: Stop as negative if the optimized verifier remains <= 1.0x speedup at q_batch >= 4 or exceeds relative L2 error 0.01.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-kv-cache-spec-decoding-co-design-for-long-context-cpu-lanes-020d08953c98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
