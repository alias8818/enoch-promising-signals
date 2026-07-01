# Operator-Doctrine Memory: Learning Reusable Behaviors Beyond Fact Recall

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-learning-reusable-behaviors-beyond-fact-recall-883b87d1d055`
Run ID: `operator-doctrine-memory-learning-reusable-behaviors-beyond-fact-recall-883b87d1d055-20260611T182818517684+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/64970e5b76f9

## What looked useful

Across 30 seeds, doctrine_tree reached 0.8729 mean accuracy versus 0.8144 for feature_kNN episode recall and 0.7641 for text_kNN fact recall, beating both on 30/30 seeds. A randomized-label control removed the advantage, with doctrine_tree at 0.1592 mean accuracy versus 0.1666 feature_kNN and 0.1689 text_kNN.

## Boundaries and scale limits

Synthetic generator only; clean structured features are available to the doctrine learner; no real operator traces, no LLM memory consumer, no long-horizon interaction, and no human doctrine extraction were tested.

## Claim scope

In a controlled synthetic operator-task benchmark with renamed factual surface forms and reusable hidden state-action doctrine, a compact induced rule memory transferred better than raw text or feature-level episode retrieval.

## Why it stopped

This run produced useful synthetic mechanism evidence, but it is proxy-only and not publication-grade validation of real operator-doctrine memory.

## Recommended next action

Run a bounded direct follow-up where both doctrine memory and fact recall are extracted from the same noisy natural-language operator traces and consumed by an LLM or agent under a fixed sequence-item budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy Text Operator-Doctrine Memory With LLM Consumer
- Success threshold: Doctrine-memory agent improves held-out action accuracy by at least 5 percentage points over the strongest fact/episode recall baseline across at least 20 seeds or equivalent paired tasks, and the randomized-label control shows no doctrine advantage.
- Stop condition: Stop if doctrine memory fails to beat the strongest recall baseline by 2 percentage points, or if gains vanish when both memories are extracted from the same noisy text.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-learning-reusable-behaviors-beyond-fact-recall-883b87d1d055`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
