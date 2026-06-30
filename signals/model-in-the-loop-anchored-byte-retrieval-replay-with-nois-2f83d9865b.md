# Model-in-the-loop anchored byte retrieval replay with noisy anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `model-in-the-loop-anchored-byte-retrieval-replay-with-nois-2f83d9865b`
Run ID: `model-in-the-loop-anchored-byte-retrieval-replay-with-nois-2f83d9865b-20260620T202302230016+0000`

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

- Parent run decision: Anchored Long-Context Cache with Byte-Exact Retrieval: enoch://control-plane/projects/anchored-long-context-cache-with-byte-exact-retrieval-64c49be9e59e/runs/anchored-long-context-cache-with-byte-exact-retrieval-64c49be9e59e-20260620T200102665941+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e65086e62ef

## What looked useful

Noisy byte anchors make exact replay fail and make naive fuzzy retrieval vulnerable to invalid close decoys. Constraining repair to valid anchors recovers most hard-regime values, but the model-loop component is not shown to add value beyond a simpler checksum-valid fuzzy baseline.

## Boundaries and scale limits

384 records, 768 invalid decoys, 640 synthetic replay queries, one seed, deterministic byte-noise model, no real LLM, no real transcript corpus, no long-horizon agent memory, CPU-only implementation.

## Claim scope

A deterministic Tier 1 synthetic byte-memory replay shows that validity-constrained anchor repair is robust to noisy anchors and invalid close decoys; the tested model-loop noise-channel repair beats naive all-anchor fuzzy retrieval but not a simpler checksum-valid fuzzy control.

## Why it stopped

Tier 1 direct test produced useful mechanism evidence but not paper-ready model-in-the-loop novelty because checksum-valid fuzzy retrieval slightly outperformed the model-loop noise-channel repair.

## Recommended next action

Run one bounded ablation that removes or weakens checksum leakage and compares a learned/model repairer against grammar-only fuzzy retrieval on the same noisy-anchor replay task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: No-checksum noisy anchor repair ablation
- Success threshold: Hard-regime top-1 accuracy lift >= 0.10 for learned/model repair versus grammar-only fuzzy retrieval, with no regression larger than 0.02 in easier regimes.
- Stop condition: Stop if grammar-only fuzzy matches or exceeds learned/model repair on at least two seeds, or if hard-regime learned/model repair remains below 0.85 top-1.

## Evidence references

- Artifact root: `<local-path>/projects/model-in-the-loop-anchored-byte-retrieval-replay-with-nois-2f83d9865b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
