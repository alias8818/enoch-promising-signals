# Agent memory with exact anchors and compressed state

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-with-exact-anchors-and-compressed-state-833fe3408680`
Run ID: `agent-memory-with-exact-anchors-and-compressed-state-833fe3408680-20260628T022612199911+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2a6832ec220d

## What looked useful

Exact anchors eliminate the bounded-summary failure mode for exact recall: compressed-only accuracy was 0.394 at summary budget 3, while anchors_plus_compressed_state and full_transcript_search both reached 1.000 exact and anchor accuracy. Anchor context averaged 213 chars versus 4232 chars for full transcript.

## Boundaries and scale limits

Synthetic parser-based benchmark only; no LLM-generated summaries, natural transcripts, vector retrieval baseline, multi-session agent loop, or large-scale workload.

## Claim scope

In a deterministic synthetic repeated-session benchmark, exact per-key anchors plus compressed state recovered exact fact values and source lines with full-transcript accuracy while using about 5% of full transcript context in the main run.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only, not a full validation of real agent memory.

## Recommended next action

Run a bounded deepen test using real LLM-generated summaries and noisy natural repeated-agent replay tasks with immutable transcript-span anchors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-summary replay test for exact anchored agent memory
- Success threshold: Anchored compressed memory reaches at least 0.90 exact-value accuracy and 0.90 citation accuracy while using at most 0.25 of full transcript context, and beats compressed-only by at least 0.20 exact accuracy.
- Stop condition: Stop if anchored memory fails to beat compressed-only by 0.10 exact accuracy on a 100-case natural replay smoke test or if citations cannot be made stable across resumes.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-with-exact-anchors-and-compressed-state-833fe3408680`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
