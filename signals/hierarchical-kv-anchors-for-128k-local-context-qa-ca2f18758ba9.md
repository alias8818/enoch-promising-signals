# Hierarchical KV Anchors for 128k Local Context QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-kv-anchors-for-128k-local-context-qa-ca2f18758ba9`
Run ID: `hierarchical-kv-anchors-for-128k-local-context-qa-ca2f18758ba9-20260603T225410904019+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/50e283a1c954

## What looked useful

At 128k, centroid anchors reached 10.9% exact retrieval while scanning 3.5% of KV and sampled anchors reached 4.1% while scanning 4.7%; increasing 128k budget to 25-31% KV scanned still stayed below 40% accuracy. Oracle chunk routing reached 100% exact retrieval while scanning 0.2% of KV, isolating the failure to anchor routing rather than within-chunk retrieval.

## Boundaries and scale limits

Synthetic retrieval only; no trained transformer, learned anchors, natural-language QA, or end-to-end generation. Main 128k probe used 512 trials, d=64 random keys, chunk_size=256, top_chunks=16, and one seed; ablation varied routing budget on one additional seed.

## Claim scope

On synthetic 16k-128k exact key-value retrieval, simple centroid and fixed-sampled hierarchical KV anchors do not reliably route noisy target-key queries to the answer block at useful compression levels; oracle block routing shows the remaining within-block retrieval step is viable.

## Why it stopped

Proxy/local evidence is sufficient to reject the naive anchor variants tested, but it is not full validation or disproof of learned hierarchical KV anchors.

## Recommended next action

Stop this run as a proxy early falsification of naive fixed/centroid KV anchors; the concrete next bounded test is a learned or query-dependent router with answer-block recall diagnostics before any natural-language QA scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned query-dependent anchor routing for 128k synthetic retrieval
- Success threshold: At 128k, achieve at least 95% answer-block recall and at least 95% exact retrieval accuracy while scanning no more than 5% of KV across at least three seeds.
- Stop condition: Stop if learned routing remains below 80% answer-block recall at 128k when scanning 5% of KV, or if the router requires scanning more than 25% of KV to exceed 95% recall.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-kv-anchors-for-128k-local-context-qa-ca2f18758ba9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
