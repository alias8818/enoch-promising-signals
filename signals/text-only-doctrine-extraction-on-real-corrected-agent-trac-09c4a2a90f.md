# Text-only doctrine extraction on real corrected agent traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `text-only-doctrine-extraction-on-real-corrected-agent-trac-09c4a2a90f`
Run ID: `text-only-doctrine-extraction-on-real-corrected-agent-trac-09c4a2a90f-20260629T151852052555+0000`

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

- Parent run decision: Trace-derived operator doctrine vs. retrieval-only memory on repeated agent tasks: enoch://control-plane/projects/trace-derived-operator-doctrine-vs-retrieval-only-memory-on-repeated-agent-tasks-b35337e7ef00/runs/trace-derived-operator-doctrine-vs-retrieval-only-memory-on-repeated-agent-tasks-b35337e7ef00-20260629T144345474727+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/237047725527

## What looked useful

Text-only doctrine recovery is feasible for transcript-echoed prompt doctrine, but naive recall is confounded by shared boilerplate and agent-message-only text recovered none of the prompt-derived doctrine.

## Boundaries and scale limits

CPU-only bounded pass over local Enoch traces; gold labels were prompt-derived lines rather than hand-labeled corrected-agent doctrine; common controller boilerplate dominated the dataset and created high mismatched-project recall.

## Claim scope

On 250 sampled local Enoch Codex traces, a deterministic text-only extractor recovered prompt-derived doctrine from full transcript text when prompts were echoed in command output, but the available traces did not contain role-tagged human correction turns.

## Why it stopped

Bounded local evidence is proxy evidence for corrected-trace doctrine extraction, not full validation; available real traces lacked user-like correction item types.

## Recommended next action

Stop this run as no-paper useful signal; next direct test should use role-tagged corrected traces with hand-labeled correction-derived doctrine and leakage-resistant controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Role-tagged corrected trace doctrine extraction benchmark
- Success threshold: Correction-derived doctrine F1 >= 0.70 and at least 0.25 absolute F1 above mismatched/boilerplate controls on held-out traces.
- Stop condition: Stop if no role-tagged correction turns are available or if boilerplate-removed F1 is below 0.50 after 50 labeled traces.

## Evidence references

- Artifact root: `<local-path>/projects/text-only-doctrine-extraction-on-real-corrected-agent-trac-09c4a2a90f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
