# Real-corpus retained-fraction test for perplexity-filtered tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-corpus-retained-fraction-test-for-perplexity-filtered-ca5c51eb95`
Run ID: `real-corpus-retained-fraction-test-for-perplexity-filtered-ca5c51eb95-20260525T005541661532+0000`

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

- Parent run decision: Perplexity-Filtered Subsets for Tiny Pretraining: enoch://control-plane/projects/perplexity-filtered-subsets-for-tiny-pretraining-c8d246260ade/runs/perplexity-filtered-subsets-for-tiny-pretraining-c8d246260ade-20260525T002327465558+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a7fbc702656d

## What looked useful

Across five seeds, low-perplexity retained subsets averaged slightly worse than random controls at both 25% (+0.170% byte perplexity) and 50% (+0.140% byte perplexity), with mixed seed wins. High-perplexity controls were usually worse at 25%, so the scorer captured some typicality signal, but low-PPL retention did not convert that signal into a robust downstream tiny-LM gain.

## Boundaries and scale limits

WikiText-2 only; byte-level n-gram scorer rather than a large pretrained scorer; tiny byte Transformer rather than GPT-2-small-class token baseline; short 500-step training budget; matched updates rather than convergence or web-scale pretraining.

## Claim scope

Tier 1 small direct test on WikiText-2: byte 5-gram perplexity filtering of train documents at 25% and 50% retained fractions did not robustly improve held-out byte-LM validation perplexity versus same-fraction random subsets for tiny byte-level Transformer pretraining under matched 500-step update budgets.

## Why it stopped

A real-corpus direct Tier 1 retained-fraction test failed to show the stated low-perplexity filtering benefit over random controls; this is an early direct falsification for the tested small setting, not a full-scale validation.

## Recommended next action

Do not write a paper from this result; only run a bounded deepen follow-up if testing whether a stronger pretrained scorer and token-level GPT-style tiny model reverses this small negative/mixed signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-level retained-fraction test with stronger perplexity scorer
- Success threshold: Low-PPL retained subsets beat random controls by at least 1% validation perplexity at both 25% and 50% retained fractions in at least 3 of 4 seeds, and high-PPL controls do not match the gain.
- Stop condition: Stop as no-paper evidence if low-PPL filtering is tied with or worse than random on either retained fraction in the aggregate, or if high-PPL controls achieve comparable gains.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-retained-fraction-test-for-perplexity-filtered-ca5c51eb95`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
