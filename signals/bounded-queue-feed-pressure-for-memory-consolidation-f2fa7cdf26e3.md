# Bounded Queue Feed Pressure for Memory Consolidation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-queue-feed-pressure-for-memory-consolidation-f2fa7cdf26e3`
Run ID: `bounded-queue-feed-pressure-for-memory-consolidation-f2fa7cdf26e3-20260620T071722509259+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/8326b63f3b9a

## What looked useful

Layered bounded consolidation achieved 0.8290 overall mean recall versus 0.5065 for bounded transcript search. It stayed at 1.0000 recall through pressure 2, then degraded to 0.9350, 0.7250, and 0.4850 at pressure 5, 10, and 20. A stricter smaller-queue variant fell to 0.4080 overall recall, showing the mechanism fails when queue pressure prevents repeated evidence from coexisting before consolidation.

## Boundaries and scale limits

Synthetic replay only; no real agent traces, embeddings, LLM attention/context effects, production memory writes, long-running sessions, or model-training evidence. Unbounded flat retrieval remained the ceiling control.

## Claim scope

In a deterministic synthetic repeated-agent replay harness with 10 stable facts, 40 seeds, five feed-pressure levels, and a 360-token bounded queue, permissive repeated-fact consolidation preserved stable facts better than bounded transcript search under distractor pressure.

## Why it stopped

Useful synthetic mechanism signal only; not direct or broad enough for a paper-ready positive result.

## Recommended next action

Run the same pressure/control matrix on real repeated-agent transcripts with measured recall and false-memory rate before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace bounded queue pressure validation for memory consolidation
- Success threshold: Layered consolidation improves stable-fact recall by at least 15 percentage points over transcript search at two or more nonzero pressure levels while keeping false-memory rate within 5 percentage points of transcript search.
- Stop condition: Stop if layered consolidation fails to beat transcript search by 10 percentage points at any nonzero pressure level or if false-memory rate exceeds transcript search by more than 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-queue-feed-pressure-for-memory-consolidation-f2fa7cdf26e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
