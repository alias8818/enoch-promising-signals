# Suffix-Match Speculative Draft Verified by Volunteer Consensus

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-match-speculative-draft-verified-by-volunteer-consensus-74e0c04f4f04`
Run ID: `suffix-match-speculative-draft-verified-by-volunteer-consensus-74e0c04f4f04-20260521T235544734968+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f075905c6213

## What looked useful

Consensus suffix acceptance is promising only as a calibrated filter or priority signal before target verification. As a replacement verifier, it fails in the important shared-bias regimes where volunteers can agree on the same wrong suffix.

## Boundaries and scale limits

No production speculative decoder, real heterogeneous volunteer model pool, latency benchmark, long-context workload, or 7B+ target model was evaluated. Tiny-GPT-2 evidence used 16 prompts repeated 8 times and artificial volunteer logit perturbations.

## Claim scope

Bounded synthetic and tiny-GPT-2 microprobe evidence: quorum suffix consensus can match target-greedy suffixes in easy, low-noise, mostly independent volunteer regimes, but it is unreliable as a no-target verifier under shared volunteer bias or margin-scale uncertainty.

## Why it stopped

Proxy and microprobe evidence are mixed: the mechanism works under near-clone or easy independent-error settings but is not robust enough to replace target verification under shared bias or margin-scale uncertainty.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement an end-to-end verifier-controlled speculative decoder on GPT-2-small-class models with real heterogeneous volunteers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end suffix consensus as a target-verified speculative decoding filter
- Success threshold: At least 10% improvement in accepted tokens per target call or wall-clock tokens/sec over standard target-verified speculative decoding, with zero post-verification false accepted tokens and no more than 5% quality degradation on the prompt set.
- Stop condition: Stop if consensus filtering provides less than 5% throughput gain over standard speculative decoding or if any unverified acceptance path is required to obtain the gain.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-match-speculative-draft-verified-by-volunteer-consensus-74e0c04f4f04`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
