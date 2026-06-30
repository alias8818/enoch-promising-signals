# Memory Architecture: Reusable Operator Doctrine vs Retrieval-Only Notes

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-architecture-reusable-operator-doctrine-vs-retrieval-only-notes-18ffc02f9ef0`
Run ID: `memory-architecture-reusable-operator-doctrine-vs-retrieval-only-notes-18ffc02f9ef0-20260628T204420165342+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/387447cd57fb

## What looked useful

On 500 tasks and 20,000 held-out predictions with 4 demonstrations per task and max operator depth 3, operator doctrine achieved 0.9954 exact accuracy and 0.9993 field accuracy versus 0.0000 exact and 0.4112 field accuracy for raw retrieval-only notes, while using about 194 bytes of induced doctrine versus 821 bytes of notes on average.

## Boundaries and scale limits

Toy CPU-only benchmark; no LLM agent, no natural-language memory, no noisy notes, no large retrieval corpus, and no stronger retrieval baseline that derives local patches from retrieved input/output pairs.

## Claim scope

In a deterministic synthetic structured-record benchmark, explicit feature-level operator doctrine generalized from few demonstrations to held-out inputs far better than raw nearest-case retrieval that copied prior note outputs.

## Why it stopped

Bounded toy evidence supports the mechanism but is insufficient for a paper or broad memory-architecture claim; the result is not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test natural-language LLM-agent memory with raw retrieval, retrieved patch inference, explicit doctrine, and hybrid memory baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language operator doctrine versus retrieval notes with stronger retrieval controls
- Success threshold: Doctrine or doctrine-hybrid improves exact held-out task success by at least 10 percentage points over raw retrieval and by at least 3 percentage points over retrieved-patch inference, without increasing memory size by more than 25%.
- Stop condition: Stop if retrieved-patch inference matches or exceeds doctrine on exact success across two seeds or if doctrine fails to beat raw retrieval by 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/memory-architecture-reusable-operator-doctrine-vs-retrieval-only-notes-18ffc02f9ef0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
