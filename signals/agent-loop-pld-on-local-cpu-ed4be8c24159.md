# Agent-Loop PLD on Local CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-loop-pld-on-local-cpu-ed4be8c24159`
Run ID: `agent-loop-pld-on-local-cpu-ed4be8c24159-20260609T123235214326+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/39c5b43f8902

## What looked useful

PLD as plateau-length distribution is cheap to compute and showed strong replicated early-warning signal for loop failure: combined AUC 0.9756 over 50,000 synthetic episodes, 95% bootstrap interval 0.9745-0.9763, with within-policy AUCs 0.8669-0.9321 where AUC was defined.

## Boundaries and scale limits

Evidence is synthetic/proxy-only: no real LLM/tool agent traces, no real task evaluator, no external benchmark, and no long-horizon production workload were tested.

## Claim scope

In a local CPU synthetic agent-loop harness, early plateau-length distribution features over the first 24 iterations predict eventual 128-step loop failure better than random and progress-only controls across replicated seeds.

## Why it stopped

Proxy-only synthetic evidence is useful for deciding the next test, but it is not direct/full validation of PLD on real agents and should not trigger paper writing.

## Recommended next action

Run the same PLD extractor on real labeled agent-loop traces and require it to beat progress-only and repeat-rate controls within task/model strata before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PLD Failure Prediction on Real Agent Traces
- Success threshold: On real traces, PLD-risk AUC >= 0.75 overall and >= 0.70 within at least three task/model strata, with at least +0.05 AUC over progress-only control and false-positive rate <= 0.15 at the selected intervention threshold.
- Stop condition: Stop as negative if PLD does not beat progress-only by at least +0.03 AUC in real trace strata or if reliable per-iteration progress/evaluator scores are unavailable.

## Evidence references

- Artifact root: `<local-path>/projects/agent-loop-pld-on-local-cpu-ed4be8c24159`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
