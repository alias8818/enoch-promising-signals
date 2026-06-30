# Prompt-Context Retrieval Draft via Embedding Cosine Top-K

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-context-retrieval-draft-via-embedding-cosine-top-k-1dadd983bdbe`
Run ID: `prompt-context-retrieval-draft-via-embedding-cosine-top-k-1dadd983bdbe-20260629T131702169251+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c3f67e44b264

## What looked useful

Embedding cosine top-k is a plausible retrieval mechanism for prompt-context drafting when queries paraphrase stored memory labels, but this run should be treated as a bounded proxy signal rather than paper-ready validation.

## Boundaries and scale limits

Synthetic corpus only; deterministic synonym-aware embedding space constructed for the benchmark; no neural embedding model, real replay transcript corpus, adversarial stale-memory control, or human/LLM draft-quality scoring. CPU-only local run completed under 15 seconds and does not validate production scale.

## Claim scope

On a deterministic synthetic replay benchmark with 400 memory chunks and 1600 paraphrased field-retrieval tasks, synonym-aware embedding cosine top-3 retrieval achieved 1.000 exact drafted-answer accuracy and 1.000 top-k recall, outperforming lexical token-overlap top-3 retrieval at 0.386 exact accuracy and 0.382 top-k recall.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic/proxy evidence and the embedding model is constructed with synonym groups, not learned from a real model or validated on real operator replay data.

## Recommended next action

Run a bounded deepen follow-up on a sanitized real replay corpus using an actual embedding model, adversarial distractors, stale-memory controls, and exact-field plus draft-quality scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Replay Embedding Top-K Retrieval With Stale-Memory Controls
- Success threshold: At least +0.15 absolute exact-answer accuracy over lexical top-k and no more than 5% stale-memory-induced wrong answers on the sanitized real replay benchmark.
- Stop condition: Stop if real embedding top-k improves exact-answer accuracy by less than 0.05 over lexical retrieval or stale/conflicting memory causes more than 15% wrong answers.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-context-retrieval-draft-via-embedding-cosine-top-k-1dadd983bdbe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
