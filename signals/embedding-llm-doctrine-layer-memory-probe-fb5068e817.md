# Embedding/LLM Doctrine-Layer Memory Probe

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `embedding-llm-doctrine-layer-memory-probe-fb5068e817`
Run ID: `embedding-llm-doctrine-layer-memory-probe-fb5068e817-20260621T155034848745+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Layered Agent Memory: Operator-Doctrine vs Flat Retrieval: enoch://control-plane/projects/layered-agent-memory-operator-doctrine-vs-flat-retrieval-d0c1ef76f1e3/runs/layered-agent-memory-operator-doctrine-vs-flat-retrieval-d0c1ef76f1e3-20260621T150032247879+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6efb0dc3fabc

## What looked useful

Best corrected dense run was E5-small with query/passage prefixes: top-1 retrieval 0.6375, top-3 retrieval 0.725, extractive answer 0.6375, shuffled-memory control 0.0125. Adding Flan-T5-small yielded only 0.0375 exact answer accuracy. The lexical diagnostic reached 1.0 top-3 but only 0.7583 top-1, suggesting the setup is recoverable but naive nearest-neighbor ranking is fragile under draft distractors.

## Boundaries and scale limits

This was a Tier 1 local direct test, not a large-corpus, production, human-authored, fine-tuned, learned-reranker, or frontier-LLM validation. It tested BGE-small and E5-small dense encoders plus Flan-T5-small, with lexical TF-IDF only as a diagnostic.

## Claim scope

In a controlled small synthetic doctrine-memory probe with 48 active doctrine records, 48 hard draft/distractor records, 240 paraphrased queries, unique randomized answer tokens, dense embedding retrieval, and a small Flan-T5 generation step, naive embedding nearest-neighbor retrieval plus LLM answering did not reliably preserve doctrine-specific bindings.

## Why it stopped

Tier 1 direct early falsification of the simple embedding/LLM doctrine-memory path: the best dense retrieval and full dense-plus-LLM run missed the stated thresholds by a wide margin, so this is no-paper useful evidence rather than paper-positive support.

## Recommended next action

Run one bounded deepen follow-up that adds metadata-aware top-k filtering or a learned/cross-encoder reranker over the same unique-token doctrine/draft benchmark, and stop unless exact answer accuracy reaches at least 0.90 with shuffled/no-memory controls near chance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Metadata-Aware Reranking for Doctrine Memory Under Draft Distractors
- Success threshold: Metadata-aware or learned reranked memory reaches >= 0.90 exact answer accuracy and >= 0.90 active-doctrine top-1 selection, while shuffled/no-memory controls remain <= 0.05.
- Stop condition: Stop as negative if reranked exact answer accuracy is < 0.85 on any of three seeds, or if gains come only from lexical leakage that does not preserve active-vs-draft doctrine selection.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-llm-doctrine-layer-memory-probe-fb5068e817`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
