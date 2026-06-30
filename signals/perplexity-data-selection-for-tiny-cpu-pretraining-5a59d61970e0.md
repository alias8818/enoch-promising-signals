# Perplexity Data Selection for Tiny CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-data-selection-for-tiny-cpu-pretraining-5a59d61970e0`
Run ID: `perplexity-data-selection-for-tiny-cpu-pretraining-5a59d61970e0-20260522T082919899789+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5479b6846b10

## What looked useful

Low/mid proxy-perplexity selection beat random by 0.105/0.125 validation bits per character in a 35% noisy candidate pool by selecting clean chunks, while high-perplexity selection failed badly. In the clean-only control, random slightly beat low-perplexity selection, so the supported mechanism is noise filtering rather than a general low-perplexity-is-best rule.

## Boundaries and scale limits

Standard-library character n-gram LM only; Tiny Shakespeare only; synthetic corruptions/noise; 8 seeds; 220,160 selected characters; no neural transformer, tokenizer, real web corpus, downstream task, or long training validation.

## Claim scope

In a bounded Tiny Shakespeare character n-gram CPU pretraining proxy with a fixed selected-character budget, proxy perplexity selection improves held-out clean validation perplexity when the candidate pool contains synthetic noisy/out-of-domain chunks, but not when all candidate chunks are already clean in-domain text.

## Why it stopped

Bounded proxy evidence is mixed: useful for identifying a noise-filtering mechanism, but insufficient and partly contrary for the broad claim that low-perplexity data selection generally improves tiny CPU pretraining.

## Recommended next action

Stop this run as a no-paper useful signal; next run should directly test the same arms on a tiny neural LM and a real mixed-quality corpus before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny neural LM perplexity selection on a real mixed-quality corpus
- Success threshold: Low_ppl or mid_ppl improves final validation loss by at least 3% versus random on the mixed-quality corpus while not underperforming random by more than 1% on the clean-only control.
- Stop condition: Stop as negative if the selected arms do not beat random on mixed-quality validation after matched-token training, or if any gain disappears in repeated seeds or is explained solely by synthetic/noisy artifacts.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-data-selection-for-tiny-cpu-pretraining-5a59d61970e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
