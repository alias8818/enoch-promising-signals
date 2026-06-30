# CompressState: running-state compression for CPU long-context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressstate-running-state-compression-for-cpu-long-context-e66db3d41033`
Run ID: `compressstate-running-state-compression-for-cpu-long-context-e66db3d41033-20260620T092312039943+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cc79cf7494ed

## What looked useful

Running-state compression is mechanically useful for exact current-state recall in sparse long histories: 1.000 accuracy over 795 synthetic queries, 5.38x fewer scanned bytes than backward transcript scan, and 0.720 accuracy for a 256-event sliding window baseline.

## Boundaries and scale limits

Synthetic symbolic events only; no real LLM, tokenizer-level prompting, learned extraction, natural transcript replay, persistent retrieval index, adversarial prompt-injection setting, or production serving workload was tested.

## Claim scope

On a deterministic synthetic CPU long-context current-state benchmark with 128 sparse user slots, compressed running state matched full transcript scan accuracy while reducing average scanned bytes from 15123.1 to 2811.4 per query; fixed sliding windows lost recall as relevant state aged out.

## Why it stopped

Closed as no-paper useful signal because the result supports the mechanism only on a synthetic proxy, not direct model-facing or production evidence.

## Recommended next action

Run a bounded natural-trace replay with model-in-the-loop state extraction and an indexed retrieval baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-trace CompressState replay with indexed retrieval control
- Success threshold: Compressed state reaches at least 0.95 current-state accuracy, stays within 0.02 absolute accuracy of the best full-context or indexed-retrieval control, and reduces query-time prompt bytes or tokens by at least 5x.
- Stop condition: Stop if compressed state accuracy falls below 0.90 or stale-update/distractor errors exceed the indexed retrieval baseline by more than 5 percentage points on the labeled replay.

## Evidence references

- Artifact root: `<local-path>/projects/compressstate-running-state-compression-for-cpu-long-context-e66db3d41033`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
