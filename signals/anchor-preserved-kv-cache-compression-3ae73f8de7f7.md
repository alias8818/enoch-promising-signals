# Anchor-Preserved KV Cache Compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-preserved-kv-cache-compression-3ae73f8de7f7`
Run ID: `anchor-preserved-kv-cache-compression-3ae73f8de7f7-20260527T160111087449+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/529125218837

## What looked useful

Across six oracle-anchor confirmation runs, anchor-preserved policies achieved 1.000 full-output label agreement and about 0.9999 cosine to full attention, while recency achieved 0.058-0.070 label agreement and stride 0.125-0.223. With 50% observed true-anchor recall plus false positives, the best anchor policy retained 0.597 label agreement versus 0.057 recency and 0.227 stride.

## Boundaries and scale limits

No pretrained transformer KV patching, no natural-language benchmark, no learned anchor detector, no multi-layer generation loop, and no serving latency/memory-system validation. The strongest result assumes oracle anchor identification; sensitivity tests show degradation when anchor recall falls.

## Claim scope

Synthetic NumPy attention probe with 512-token contexts, 6.25%-12.5% KV budgets, explicit old anchor tokens, and recent distractors: preserving observed anchors approximates full attention much better than pure recency or stride when the query depends on an old anchor.

## Why it stopped

Closed as a no-paper useful signal because the evidence is synthetic attention-level mechanism evidence, not direct language-model or serving evidence.

## Recommended next action

Run a bounded direct-evidence follow-up by patching a small pretrained decoder's KV cache on a natural long-context retrieval/copy benchmark, using rule-based anchors and equal-budget recency, stride, and heavy-hitter baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Decoder KV Patch Test for Anchor-Preserved Compression
- Success threshold: At 12.5% KV budget, anchor-preserved compression improves exact-match retrieval accuracy by at least 20 percentage points over both recency and stride, while losing no more than 10 percentage points versus full cache on the same prompts.
- Stop condition: Stop if anchor-preserved compression fails to beat the best equal-budget baseline by at least 5 percentage points on a 200-prompt small-model benchmark or if KV patching cannot preserve model correctness in a reproducible smoke test.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserved-kv-cache-compression-3ae73f8de7f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
