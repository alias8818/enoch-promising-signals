# Suffix-Array N-Gram Speculative Decoding for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-n-gram-speculative-decoding-for-cpu-inference-ff9107621370`
Run ID: `suffix-array-n-gram-speculative-decoding-for-cpu-inference-ff9107621370-20260610T064729875702+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb42f9c0ae34

## What looked useful

Prompt n-gram speculation can provide non-trivial accepted draft tokens when outputs reuse prompt spans; suffix arrays preserve that mechanism with a compact index, but the measured CPU path was 13.4x slower per lookup and 7.5x slower to build than a hash n-gram baseline on the medium grid.

## Boundaries and scale limits

Proxy-only benchmark: no LLM forward passes, no real prompt corpus, no KV-cache or serving integration, single-process Python implementation, and synthetic exact-token acceptance only.

## Claim scope

On deterministic synthetic prompt-copy token traces up to 160k prompt tokens, suffix-array prompt lookup matched multi-order hash n-gram draft quality and used much less estimated payload memory, but was substantially slower to build and query in the tested CPU implementation.

## Why it stopped

Synthetic/proxy evidence supports a compact-memory mechanism but not a direct or paper-ready CPU inference speedup claim; the simpler hash n-gram baseline is faster in all local tests.

## Recommended next action

Stop as no-paper useful signal; only continue with a bounded C++/Rust serving-stack follow-up that must beat the hash baseline on end-to-end CPU tokens/s or demonstrate a memory-bound regime where the suffix-array tradeoff wins.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: C++ suffix-array prompt lookup in a CPU LLM decode loop
- Success threshold: Suffix-array variant achieves at least 10% end-to-end tokens/s improvement over the hash n-gram baseline or at least 3x lower memory at statistically indistinguishable latency on real long-prompt CPU inference traces.
- Stop condition: Stop if optimized suffix-array lookup remains more than 2x slower than hash lookup without a measured memory-bound end-to-end win.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-n-gram-speculative-decoding-for-cpu-inference-ff9107621370`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
