# Real-verifier bounded suffix-history drafting on small code and prose corpora

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-verifier-bounded-suffix-history-drafting-on-small-cod-798b617d0d`
Run ID: `real-verifier-bounded-suffix-history-drafting-on-small-cod-798b617d0d-20260619T145901415106+0000`

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

- Parent run decision: Bounded suffix-tree draft with no extra model weights: enoch://control-plane/projects/bounded-suffix-tree-draft-with-no-extra-model-weights-b84fef66e120/runs/bounded-suffix-tree-draft-with-no-extra-model-weights-b84fef66e120-20260619T142037736994+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/999e8a3b4411

## What looked useful

Best suffix-history setting reached 3.0216x no-draft verifier-call speedup on code and 1.8694x on prose, beating the bigram control by 129.8% and 75.6% respectively and exceeding the predeclared accepted-bytes-per-call threshold on both corpora.

## Boundaries and scale limits

Raw-byte tokenization, 120k-byte history plus 40k-byte held-out test per corpus, local Python/doc corpus slices, exact continuation verifier only; no neural target model, model tokenizer, KV-cache, batching, or wall-clock decoding throughput validation.

## Claim scope

On two small local byte-level corpora, one code and one prose, a bounded suffix-history drafter using only prior history reduced exact held-out verifier calls more than unigram and history-only bigram controls.

## Why it stopped

Tier 1 direct small-corpus exact-verifier threshold was met, but evidence remains no-paper because neural verification and end-to-end decoding throughput were not tested.

## Recommended next action

Run a bounded model-token follow-up with a small causal LM verifier and the same corpora to test whether suffix-history gains survive realistic tokenization and verifier latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-token suffix-history drafting with a small causal LM verifier
- Success threshold: Suffix-history improves verifier-call speedup or end-to-end tokens/sec by at least 25% over the bigram control on both code and prose without index overhead erasing the gain.
- Stop condition: Stop if suffix-history fails to beat bigram by 10% on either corpus, or if measured indexing/proposal overhead makes end-to-end throughput no better than no-draft decoding.

## Evidence references

- Artifact root: `<local-path>/projects/real-verifier-bounded-suffix-history-drafting-on-small-cod-798b617d0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
