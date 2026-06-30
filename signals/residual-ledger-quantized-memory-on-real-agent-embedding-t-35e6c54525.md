# Residual-ledger quantized memory on real agent embedding traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-ledger-quantized-memory-on-real-agent-embedding-t-35e6c54525`
Run ID: `residual-ledger-quantized-memory-on-real-agent-embedding-t-35e6c54525-20260522T112907227722+0000`

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

- Parent run decision: Quantized agent memory with residual error ledger: enoch://control-plane/projects/quantized-agent-memory-with-residual-error-ledger-4bff6a1d61b5/runs/quantized-agent-memory-with-residual-error-ledger-4bff6a1d61b5-20260522T112005526066+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4286aa1c5b71

## What looked useful

Residual ledger entries reduced vector reconstruction error, but nearest-neighbor recall gains were small. Within the 25% storage cap, the best residual setting improved recall@10 by only 0.875 percentage points and reconstruction error by 9.32%, below the 5 percentage-point and 15% thresholds. The 16-entry variant reduced reconstruction error by 17.7% but exceeded the storage cap and lifted recall by only 1.5 points.

## Boundaries and scale limits

No production embedding model, no online agent-memory loop, no adversarial trace mix, and no large-scale serving workload. The test is a local deterministic embedding-trace proxy over real agent logs, not publication-grade validation.

## Claim scope

Controlled Tier 1 test on 4,000 chunks from 34 local real Enoch/Codex agent trace JSONL files using deterministic 384-dimensional signed-hash embeddings. Int4 residual-ledger variants improved reconstruction cosine but did not meet the pre-set recall@10 and storage thresholds against plain int4.

## Why it stopped

Scoped early falsification: on real agent trace derived embeddings, the residual-ledger mechanism improved reconstruction but failed the direct retrieval threshold under the storage cap. This is not a full validation or universal negative.

## Recommended next action

Run one bounded deepen test on real sentence-transformer or production-style embeddings with the same storage-capped recall threshold; stop if recall lift remains under 5 percentage points.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-ledger recall on real model embeddings
- Success threshold: At <=25% storage overhead over plain int4 and smaller than plain int8, residual-ledger memory improves recall@10 by at least 5 percentage points and reduces reconstruction cosine error by at least 15% versus plain int4.
- Stop condition: Stop as negative if the best storage-capped residual-ledger variant improves recall@10 by less than 5 percentage points or if reconstruction gains again fail to transfer to retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/residual-ledger-quantized-memory-on-real-agent-embedding-t-35e6c54525`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
