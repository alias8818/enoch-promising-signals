# Proxy-Loss Domain Mixing Balances Tiny Local Corpora

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `proxy-loss-domain-mixing-balances-tiny-local-corpora-d2ac3fc1954d`
Run ID: `proxy-loss-domain-mixing-balances-tiny-local-corpora-d2ac3fc1954d-20260601T060731949329+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aa233e0bb664

## What looked useful

Proxy-loss adaptation can rebalance underrepresented domains, but in this bounded setting it mostly converged near equal-domain sampling. Uniform-domain sampling should be a required control for future tiny-corpus domain-mixing claims.

## Boundaries and scale limits

Synthetic corpora only; one small bigram softmax model class; 8 seeds; 1600 update steps; no real local text, transformer-scale model, downstream task, or long-run training validation.

## Claim scope

In a deterministic synthetic three-domain tiny-corpus NumPy bigram language-model proxy, proxy-loss adaptive domain sampling materially improved rare-domain and worst-domain held-out loss versus size-proportional sampling, but did not meaningfully outperform a simple uniform-domain sampler.

## Why it stopped

Proxy-only synthetic result is mixed: adaptive strongly beats size-proportional sampling but provides negligible novelty over uniform-domain sampling, so it is an early bounded no-paper result rather than full validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded evidence should test real tiny local corpora and require proxy-loss adaptation to beat uniform-domain sampling, not only size-proportional sampling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tiny-corpus proxy-loss mixing against uniform-domain control
- Success threshold: Proxy-loss adaptive sampling improves worst-domain held-out loss by at least 0.03 cross entropy versus uniform-domain sampling on at least 75% of paired seeds, while macro loss is no worse than +0.01.
- Stop condition: Stop as negative if adaptive fails to beat uniform-domain sampling by the threshold, or if any gain is explained by a static near-uniform mixture.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-loss-domain-mixing-balances-tiny-local-corpora-d2ac3fc1954d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
