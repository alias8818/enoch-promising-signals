# Naturalistic Paraphrase Memory Grounding With End-to-End Answer Metrics

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `naturalistic-paraphrase-memory-grounding-with-end-to-end-a-45f563a044`
Run ID: `naturalistic-paraphrase-memory-grounding-with-end-to-end-a-45f563a044-20260519T124136613061+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Naturalistic Paraphrase Memory Grounding With End-to-End Answer Metrics: internal_generated:naturalistic-paraphrase-memory-grounding-with-end-to-end-a-45f563a044

## What looked useful

Paraphrase-augmented memory achieved 0.60822 mean exact answer accuracy versus 0.14032 for canonical memory, with paired bootstrap treatment-minus-baseline delta about +0.468. The shuffled-answer control scored 0.02416 answer accuracy despite 0.72396 relation accuracy, supporting that the end-to-end metric detects grounding failures. Relation-level results were uneven, especially for discovery questions.

## Boundaries and scale limits

Validated on 5 fixed seeds, 1,000 entities per seed, 5,000 facts per seed, and 50,000 total held-out QA trials using a pure retrieval-plus-extraction system. Not validated on human-authored natural corpora, learned retrievers, LLM generation, adversarial distractors, or equal-token-budget memory controls.

## Claim scope

In a templated synthetic fact-memory QA setting with held-out paraphrase questions, indexing paraphrased memory variants substantially improved retrieval-grounded exact answer accuracy over a canonical lexical memory baseline, while shuffled-answer memory collapsed end-to-end answer accuracy.

## Why it stopped

Moderate direct evidence supports the mechanism in a templated bounded setting, but synthetic data, unequal memory text budget, and weak relation families prevent publication-grade closure.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded deepen test should use a natural paraphrase QA corpus with equal-token-budget memory controls and a learned retriever or LLM-RAG baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural Corpus Paraphrase Memory Grounding With Equal-Budget Controls
- Success threshold: Paraphrase memory must improve exact answer accuracy by at least +0.10 over both canonical and equal-token-budget controls, with the paired 95% confidence interval lower bound above +0.05 across at least three seeds and no category showing shuffled-control-like collapse.
- Stop condition: Stop if equal-token-budget controls erase the answer-accuracy gain, if shuffled-answer controls do not collapse answer accuracy, or if natural paraphrase categories reproduce the weak discovery-style failure pattern in most categories.

## Evidence references

- Artifact root: `<local-path>/projects/naturalistic-paraphrase-memory-grounding-with-end-to-end-a-45f563a044`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
