# Natural-noise neural-scorer low-perplexity filtering test for tiny GPT pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-noise-neural-scorer-low-perplexity-filtering-test-1a6497e803`
Run ID: `natural-noise-neural-scorer-low-perplexity-filtering-test-1a6497e803-20260522T212239379439+0000`

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

- Parent run decision: Perplexity-based data filtering for tiny local pretraining: enoch://control-plane/projects/perplexity-based-data-filtering-for-tiny-local-pretraining-c3069ea96744/runs/perplexity-based-data-filtering-for-tiny-local-pretraining-c3069ea96744-20260522T203135046009+0000
- Parent run decision: Medium-scale low-perplexity filtering confirmation for tiny pretraining: enoch://control-plane/projects/medium-scale-low-perplexity-filtering-confirmation-for-tin-b7ddca2259/runs/medium-scale-low-perplexity-filtering-confirmation-for-tin-b7ddca2259-20260522T204651428591+0000

## What looked useful

At 1000 target steps, neural_lowppl_filter achieved mean clean validation PPL 9.1168 versus 9.5218 for unfiltered_matched, a 4.25% reduction, and beat random_filter and heuristic_filter in all three seeds. The scorer also removed all HTML-injection samples and reduced kept-set scorer loss from about 2.47-2.49 to about 1.86-1.88.

## Boundaries and scale limits

The corpus is small and domain-narrow, noise is synthetically injected rather than sampled from a real web crawl, the target model is character-level and far below GPT-2-small scale, and only three seeds were run. This does not establish production-scale or paper-ready pretraining data filtering.

## Claim scope

In a self-contained Tiny Shakespeare character-level tiny GPT setup with injected natural text noise, a GRU clean-text neural scorer used to keep the lowest-perplexity half of candidate sequences improved clean held-out validation perplexity versus equal-token unfiltered, random-filter, and heuristic-filter controls across three fixed seeds.

## Why it stopped

Local Tier 2 evidence supports the mechanism and passed the bounded 1000-step threshold, but the setup remains too small and synthetic-noise-dependent for a paper-positive decision.

## Recommended next action

Run a deepen follow-up using a GPT-2-small-class BPE-tokenized model on a real noisy web/text corpus with the same equal-token baselines and a preregistered >=3% clean validation perplexity improvement threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class neural low-perplexity filtering on real noisy text
- Success threshold: Neural low-perplexity filtering must reduce mean clean validation perplexity by at least 3% versus equal-token unfiltered and beat random and heuristic filters in most fixed seeds without relying on synthetic-only noise.
- Stop condition: Stop if neural filtering fails to beat unfiltered by 3% mean clean validation perplexity, fails to beat random/heuristic controls in most seeds, or selection diagnostics show the effect is explained by a trivial heuristic.

## Evidence references

- Artifact root: `<local-path>/projects/natural-noise-neural-scorer-low-perplexity-filtering-test-1a6497e803`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
