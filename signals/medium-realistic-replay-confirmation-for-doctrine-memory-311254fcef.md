# Medium realistic replay confirmation for doctrine memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-realistic-replay-confirmation-for-doctrine-memory-311254fcef`
Run ID: `medium-realistic-replay-confirmation-for-doctrine-memory-311254fcef-20260619T084200283982+0000`

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

- Parent run decision: Operator-Doctrine Memory vs Flat Retrieval for Tiny Agent: enoch://control-plane/projects/operator-doctrine-memory-vs-flat-retrieval-for-tiny-agent-a88c41f19d87/runs/operator-doctrine-memory-vs-flat-retrieval-for-tiny-agent-a88c41f19d87-20260619T082032420365+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8977943e21b7

## What looked useful

Layered doctrine memory achieved 1.0000 full accuracy versus 0.6000 for the best non-layered baseline, exceeding the Tier-1 threshold of at least 0.80 full accuracy and at least 0.20 margin.

## Boundaries and scale limits

Small controlled local corpus only; no live LLM agent, embeddings, production traces, long-horizon memory growth, cross-domain replay distribution, or deployment latency was tested.

## Claim scope

In a controlled Tier-1 replay corpus of 4 scenarios and 10 confirmation queries, deterministic layered doctrine memory correctly preserved confirmed facts, rejected tentative/stale/noisy facts, handled exact-claim retractions, and cited supporting sessions better than no-memory, transcript-search, and flat-retrieval controls.

## Why it stopped

Tier-1 controlled direct evidence supports the mechanism, but the result is a useful no-paper signal rather than paper-positive validation.

## Recommended next action

Run one bounded deepen follow-up on at least 50 semi-natural replay queries with paraphrased doctrine and an LLM or retrieval answerer; stop if layered memory fails to maintain 0.80 full accuracy or a 0.15 margin over the best non-layered baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semi-natural replay confirmation for layered doctrine memory
- Success threshold: Layered doctrine memory full accuracy >= 0.80 and margin over the best non-layered baseline >= 0.15 on at least 50 labeled replay queries.
- Stop condition: Stop as negative/no-paper if layered memory full accuracy is below 0.80 or its margin over the best non-layered baseline is below 0.15 after the corpus and scoring checks pass.

## Evidence references

- Artifact root: `<local-path>/projects/medium-realistic-replay-confirmation-for-doctrine-memory-311254fcef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
