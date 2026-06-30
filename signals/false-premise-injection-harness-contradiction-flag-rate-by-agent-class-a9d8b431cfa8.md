# False-Premise Injection Harness: Contradiction-Flag Rate by Agent Class

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `false-premise-injection-harness-contradiction-flag-rate-by-agent-class-a9d8b431cfa8`
Run ID: `false-premise-injection-harness-contradiction-flag-rate-by-agent-class-a9d8b431cfa8-20260630T032951993256+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fb5311bfaa9a

## What looked useful

A reproducible local harness now measures false-premise contradiction-flag rate and clean-control false-positive rate by agent class. It exposes a practical distinction between compliant, transcript-literal, flat-retrieval, alias-aware layered-memory, and overcautious guard policies.

## Boundaries and scale limits

Synthetic deterministic rules only; no live LLM agents, no broad fact corpus, no human-blinded labeling, no long-context or multi-turn adversarial evaluation.

## Claim scope

In a deterministic 96-case synthetic replay harness, contradiction-flag rate differs sharply by agent memory/retrieval policy class; alias-aware layered memory flagged all false premises with zero clean-control false positives, while flat canonical retrieval dropped on alias-shifted cases and no-memory compliance missed all false premises.

## Why it stopped

Scoped useful signal only: the result validates the harness and deterministic mechanism, but it is proxy/synthetic evidence rather than direct live-agent validation.

## Recommended next action

Run the same harness against live LLM-backed agent implementations with matched prompts, paraphrased false premises, and blinded/manual review of contradiction flags.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-agent false-premise contradiction flag benchmark
- Success threshold: A retrieval or layered-memory live-agent class improves false-premise flag rate by at least 25 percentage points over no-memory compliance while keeping clean-control false-positive rate below 10%.
- Stop condition: Stop if live-agent outputs do not preserve a measurable gap between memory/retrieval classes, or if clean-control false-positive rates exceed 10% for all high-recall variants.

## Evidence references

- Artifact root: `<local-path>/projects/false-premise-injection-harness-contradiction-flag-rate-by-agent-class-a9d8b431cfa8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
