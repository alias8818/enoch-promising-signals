# Proxy Perplexity Resampling for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `proxy-perplexity-resampling-for-tiny-pretraining-90ae45c68036`
Run ID: `proxy-perplexity-resampling-for-tiny-pretraining-90ae45c68036-20260531T191741447054+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/074b42fbf6bb

## What looked useful

Proxy perplexity is a real sampling lever, but naive easy-chunk resampling is not supported. The promising variant is diversity-constrained high-proxy-perplexity oversampling: temperature 2.0 high-proxy sampling improved validation NLL by 0.0839 versus uniform across three seeds, while temperature 1.0 collapsed effective sample size to about 1.1 and failed badly.

## Boundaries and scale limits

Short 350-step runs, byte-level GRU rather than tokenizer-based transformer, Wikitext-2 only, 7000 train chunks and 1200 validation chunks, two sampling temperatures, no GPT-2-small-class or long-horizon validation.

## Claim scope

Bounded local evidence from byte-level tiny GRU language-model pretraining on Wikitext-2: proxy perplexity resampling materially changes validation loss, low-proxy/easy-chunk oversampling did not beat uniform, aggressive high-proxy oversampling collapsed sample diversity, and softened high-proxy oversampling improved validation loss across three seeds.

## Why it stopped

No paper-positive closure: this run is a bounded tiny-model signal, not full validation. It locally falsifies low-proxy/easy-chunk resampling and identifies a specific softened high-proxy variant worth one direct follow-up.

## Recommended next action

Run a bounded deepen follow-up with a tokenizer-based small transformer and an explicit effective-sample-size floor for high-proxy-perplexity sampling; stop if it does not beat uniform by at least 0.03 validation NLL across three seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-Constrained High-Proxy-Perplexity Resampling for Tiny Transformer Pretraining
- Success threshold: ESS-constrained high-proxy sampling beats uniform validation NLL by at least 0.03 mean NLL across three seeds without any seed regressing by more than 0.01 NLL.
- Stop condition: Stop as negative if the constrained high-proxy policy fails the success threshold or if its gain disappears when matched for effective sample size.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-perplexity-resampling-for-tiny-pretraining-90ae45c68036`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
