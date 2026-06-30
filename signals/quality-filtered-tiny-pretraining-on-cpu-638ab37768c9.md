# Quality-filtered tiny pretraining on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-filtered-tiny-pretraining-on-cpu-638ab37768c9`
Run ID: `quality-filtered-tiny-pretraining-on-cpu-638ab37768c9-20260530T010847274843+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6d56167698b4

## What looked useful

Filtered training won 3/3 seeds on contaminated candidate pools, improving validation NLL by 0.0693 +/- 0.0073 and increasing selected clean-document fraction by 0.477. A clean-only control showed negligible mean NLL improvement of 0.0010, indicating the observed benefit is primarily contamination removal.

## Boundaries and scale limits

Synthetic low-quality documents, Tiny Shakespeare clean distribution, three seeds, 250k selected training tokens per arm, 350 update steps, byte-level n-gram-style neural LM rather than a transformer; no real web corpus or downstream task validation.

## Claim scope

On a tiny NumPy byte-level causal LM trained on CPU, simple quality filtering improved held-out clean Tiny Shakespeare validation NLL under an equal-token budget when the candidate pretraining stream contained 50% generated low-quality corruptions.

## Why it stopped

Closed as no-paper useful signal because the evidence is direct for the local tiny synthetic-contamination mechanism but not broad or publication-grade for quality-filtered pretraining.

## Recommended next action

Run a bounded deepen test on a real small corpus with real or classifier-derived quality labels and a parameter-matched tiny transformer before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus quality filtering for a tiny transformer under equal-token CPU pretraining
- Success threshold: Filtered arm wins at least 3/3 seeds with mean validation NLL improvement >= 0.03 under equal-token training and no comparable gain on clean-only controls.
- Stop condition: Stop if filtered selection fails to improve mean validation NLL by 0.01 or if gains also appear on clean-only controls, indicating sample bias rather than quality filtering.

## Evidence references

- Artifact root: `<local-path>/projects/quality-filtered-tiny-pretraining-on-cpu-638ab37768c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
