# N-gram Proxy Quality Filtering

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-proxy-quality-filtering-e3811047c4a3`
Run ID: `n-gram-proxy-quality-filtering-e3811047c4a3-20260528T175500962766+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/10efd384d24c

## What looked useful

N-gram proxy ranking recovered a real domain signal: best proxy purity was 0.365 versus random mean 0.247, and proxy-bottom purity was about 0.15. However, best proxy held-out trigram perplexity improved only 2.8% over the random median, below the 10% success threshold, with 4 of 30 random trials as good or better; length_top achieved better perplexity with near-random purity.

## Boundaries and scale limits

CPU-only word n-gram experiment; 80 seed documents, 1,029 candidate documents, 229 held-out target documents, one target domain, topic labels used as the quality proxy, no neural LM training, no web-scale or human-quality labels.

## Claim scope

On a bounded 20 Newsgroups topic-filtering proxy, a seed word n-gram scorer increased target-domain selection purity but did not meet the predeclared downstream perplexity improvement threshold and was beaten by a simple length baseline.

## Why it stopped

Proxy/local evidence is mixed: n-gram filtering improves target purity, but downstream word-trigram perplexity gain is small, below threshold, baseline-sensitive, and not a full validation of corpus quality filtering.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing, run a bounded neural-LM follow-up with length-matched controls before making any quality-filtering claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-matched neural LM test of n-gram proxy filtering
- Success threshold: Proxy filtering improves held-out neural LM validation perplexity by at least 5% versus random median and beats length baselines in at least two target domains while preserving a clear purity lift.
- Stop condition: Stop if proxy filtering does not beat both random and length controls in the first two target domains or if gains are within random-seed noise.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-proxy-quality-filtering-e3811047c4a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
