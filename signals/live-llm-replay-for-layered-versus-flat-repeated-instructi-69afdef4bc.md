# Live LLM replay for layered versus flat repeated-instruction memory

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `live-llm-replay-for-layered-versus-flat-repeated-instructi-69afdef4bc`
Run ID: `live-llm-replay-for-layered-versus-flat-repeated-instructi-69afdef4bc-20260630T023902346737+0000`

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

- Parent run decision: Layered memory reduces repeated instructions vs flat vector retrieval: enoch://control-plane/projects/layered-memory-reduces-repeated-instructions-vs-flat-vector-retrieval-ed3d436d7394/runs/layered-memory-reduces-repeated-instructions-vs-flat-vector-retrieval-ed3d436d7394-20260629T170032095110+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/218ac87ce6e2

## What looked useful

The live replay found a ceiling effect: flat noisy repeated-instruction prompts were already solved perfectly, so these tasks are too easy to distinguish layered memory from flat memory.

## Boundaries and scale limits

Single available Codex CLI model, four synthetic paired cases, prompt-supplied memory only, no autonomous memory update loop, no embedding retrieval, no human trace corpus, and no multi-model replication.

## Claim scope

On four small synthetic live Codex replay cases, both flat repeated-instruction memory and layered memory recovered all current fields exactly; the tested prompt design does not show a layered-memory advantage.

## Why it stopped

Bounded live replay produced an early negative/ceiling-effect result for the easy synthetic comparison, not a full validation of layered memory.

## Recommended next action

Stop this run as a no-paper ceiling-effect result; if continuing, run a harder paired live replay with longer shuffled flat memories and at least 20 cases before revisiting the layered-memory claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder live replay for layered memory under shuffled stale instruction pressure
- Success threshold: Layered exact rate exceeds flat exact rate by at least 0.25 with no increase in parse failures and with at least 20 paired cases completed.
- Stop condition: Stop as negative if flat exact rate remains within 0.10 of layered exact rate, or if both conditions remain above 0.90 exact on the harder corpus.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-replay-for-layered-versus-flat-repeated-instructi-69afdef4bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
