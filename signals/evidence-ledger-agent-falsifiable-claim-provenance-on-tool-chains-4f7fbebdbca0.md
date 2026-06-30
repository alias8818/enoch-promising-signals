# Evidence-Ledger Agent: Falsifiable Claim Provenance on Tool Chains

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-falsifiable-claim-provenance-on-tool-chains-4f7fbebdbca0`
Run ID: `evidence-ledger-agent-falsifiable-claim-provenance-on-tool-chains-4f7fbebdbca0-20260619T110754211315+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/06fb855ec8bb

## What looked useful

On 30,000 synthetic claims over 25,000 tool observations, the ledger verifier achieved 1.0 exact verdict accuracy and 0.0 supported-claim false positives/false negatives; the naive provenance baseline had 0.3333333333333333 supported-claim accuracy and 0.8 false positive rate.

## Boundaries and scale limits

Synthetic deterministic traces only; no real LLM claim extraction, natural-language ambiguity, adversarial tool outputs, multi-hop agent traces, LangGraph integration overhead, or human-labeled transcript benchmark.

## Claim scope

A deterministic evidence ledger can distinguish supported, contradicted, unsupported, missing, stale, and tampered claims on synthetic structured tool-chain traces, outperforming a naive provenance baseline that treats any present evidence id as support.

## Why it stopped

Proxy synthetic evidence supports the mechanism but is not direct real-agent validation and should not be presented as full validation or publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; next, evaluate the ledger on a small real-agent transcript corpus with independent claim labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent transcript evaluation for evidence-ledger claim provenance
- Success threshold: At least 50% reduction in unsupported supported-claim false positives versus baseline, supported-claim false negative rate no higher than 10%, and p95 verifier latency below 50 ms per claim on the corpus.
- Stop condition: Stop as negative if claim extraction cannot map at least 70% of labeled claims to verifiable predicates or if the ledger fails to reduce false positives by 25% versus the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-falsifiable-claim-provenance-on-tool-chains-4f7fbebdbca0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
