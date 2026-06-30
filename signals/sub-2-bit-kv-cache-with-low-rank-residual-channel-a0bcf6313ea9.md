# Sub-2-bit KV-cache with Low-Rank Residual Channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-2-bit-kv-cache-with-low-rank-residual-channel-a0bcf6313ea9`
Run ID: `sub-2-bit-kv-cache-with-low-rank-residual-channel-a0bcf6313ea9-20260621T143600384786+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/59f15e12bd75

## What looked useful

Rank-2 residual improved mean attention-output relative L2 versus pure 1-bit by 1.8% on Gaussian synthetic K/V, 20.8% on structured low-rank K/V, and 6.2% on outlier K/V at 1.8125 effective bits/value. This supports the residual-channel mechanism only as a bounded synthetic signal; absolute errors remained high.

## Boundaries and scale limits

No pretrained transformer, real KV trace, perplexity/task metric, online residual update, GPU kernel, latency, or memory-bandwidth evidence was produced. The low-rank residual used offline SVD over the full cache and the 2-bit baseline was a simple rowwise uniform quantizer.

## Claim scope

Synthetic NumPy attention-fidelity probe over 512-token, 64-dimensional K/V tensors shows that a 1-bit rowwise KV cache plus fp16 rank-1 or rank-2 residual channel can reduce attention-output error below the pure 1-bit baseline while staying under 2 effective bits/value.

## Why it stopped

Synthetic proxy evidence is useful but insufficient for a paper or production claim; the run closes as no-paper useful signal rather than full validation.

## Recommended next action

Run a bounded real-transformer KV trace follow-up with an online low-rank residual update, perplexity or next-token-loss metrics, and a stronger 2-bit KV quantization baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer KV trace test for sub-2-bit low-rank residual cache
- Success threshold: At less than 2 effective bits/value, reduce next-token-loss degradation by at least 25% versus pure 1-bit and stay within 10% relative degradation of a strong 2-bit KV baseline on the same prompts.
- Stop condition: Stop if online residual updates fail to improve loss degradation by at least 10% versus pure 1-bit on a smoke set, or if memory accounting reaches 2 or more effective bits/value.

## Evidence references

- Artifact root: `<local-path>/projects/sub-2-bit-kv-cache-with-low-rank-residual-channel-a0bcf6313ea9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
