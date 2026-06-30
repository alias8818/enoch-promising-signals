# Tiny encoder for 4k-to-1k context compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-encoder-for-4k-to-1k-context-compression-ecadfdd1c019`
Run ID: `tiny-encoder-for-4k-to-1k-context-compression-ecadfdd1c019-20260602T204911002115+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4174e93ed6b9

## What looked useful

Learned compression reached 0.9261 mean token reconstruction accuracy across 3 seeds, versus 0.2557 for mean pooling and 0.2529 for subsampling at the same 4096-to-1024 token compression ratio. An initial sparse associative retrieval calibration remained at chance and was not treated as a definitive negative.

## Boundaries and scale limits

Tested only on synthetic random token reconstruction with vocabulary size 256, dim 64, group size 4, 500 train steps, batch size 32, 3 seeds, and a small MLP encoder/decoder. It does not validate natural-language context compression, downstream next-token prediction, QA, retrieval, or GPT-2-small-class baselines.

## Claim scope

On a synthetic reconstruction proxy, a tiny learned 4-token-to-1-latent encoder compresses 4096 random tokens into 1024 latent vectors and reconstructs held-out tokens substantially better than fixed mean or subsample 4x compression controls.

## Why it stopped

No-paper useful signal: evidence supports the reconstruction mechanism on a synthetic proxy but is not direct/full validation of practical 4k-to-1k LLM context compression.

## Recommended next action

Run a bounded deepen follow-up that evaluates compressed 1024-latent memory on downstream retrieval or next-token loss with a small decoder and full-context/fixed-compression controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Downstream retrieval test for 4k-to-1k learned context compression
- Success threshold: Learned compression improves held-out downstream retrieval accuracy or next-token loss by at least 20 percentage points or 20% relative loss reduction versus both fixed 4x controls, while preserving at least 80% of the full-context control performance.
- Stop condition: Stop if learned compression fails to beat both fixed controls after a calibrated short run and one architecture adjustment, or if full-context control itself fails to learn the task.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-encoder-for-4k-to-1k-context-compression-ecadfdd1c019`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
