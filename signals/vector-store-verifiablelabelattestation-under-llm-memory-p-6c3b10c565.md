# Vector-store VerifiableLabelAttestation under LLM memory poisoning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `vector-store-verifiablelabelattestation-under-llm-memory-p-6c3b10c565`
Run ID: `vector-store-verifiablelabelattestation-under-llm-memory-p-6c3b10c565-20260619T175803653309+0000`

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

- Parent run decision: VerifiableLabelAttestation: enoch://control-plane/projects/verifiablelabelattestation-0ad25d9da43b/runs/verifiablelabelattestation-0ad25d9da43b-20260619T173447550534+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/8a8b14f4b5cd

## What looked useful

Content-bound VLA achieved 80/80 correct retrievals with 0/80 poison selections; vector-only and spoofable-label baselines selected poisons 80/80 times; label-only VLA also selected poisons 80/80 times through replayed label attestations.

## Boundaries and scale limits

Synthetic templated memories, hashing bag-of-words embeddings, in-memory retrieval, no real vector database, no live LLM attacker, and no LLM answer generation from retrieved context.

## Claim scope

In a deterministic 80-task synthetic vector-store memory poisoning test, visible label filtering and label-only attestation were bypassed, while content-bound label attestation prevented poison selection.

## Why it stopped

Tier 1 controlled direct test produced a useful mechanism signal, but evidence remains synthetic and not publication-grade.

## Recommended next action

Run a medium confirmation using a real embedding model and vector database with paraphrased/adaptive poisoned memories and LLM answer generation from retrieved context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-vector-store confirmation of content-bound VLA against memory poisoning
- Success threshold: Content-bound VLA poison selection <= 5%, clean retrieval accuracy >= 95%, and answer accuracy >= 90% under poisoned retrieval contexts.
- Stop condition: Stop if content-bound verification fails to reject replayed or tampered poison artifacts, or if clean retrieval accuracy falls below 90% before attack evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/vector-store-verifiablelabelattestation-under-llm-memory-p-6c3b10c565`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
