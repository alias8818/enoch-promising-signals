# Small-agent evidence ledger with local policy verifier

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-agent-evidence-ledger-with-local-policy-verifier-e1aa4e5ce2e1`
Run ID: `small-agent-evidence-ledger-with-local-policy-verifier-e1aa4e5ce2e1-20260528T215021459416+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0390c3e9c4a0

## What looked useful

Corrected multi-seed run produced 44,927 true rejects, 5,073 true allows, 0 false allows, 0 false rejects, mean verifier latency 0.837 us/action, mean throughput 135,852 actions/s, and hash-chain mutation detection in every seed.

## Boundaries and scale limits

Only synthetic local traces were tested: 50,000 actions across 5 seeds, one process, no real LLM agents, no adversarial prompt-injection traces, no signed/distributed ledger, no production tool semantics, and no realistic ambiguous policy corpus.

## Claim scope

In a deterministic synthetic small-agent action stream with explicit evidence references, an append-only evidence ledger plus local policy verifier rejected unsupported or unsafe actions across evidence presence, hash consistency, subject match, source trust, freshness, asserted value, tool allowlist, spend cap, and simple PII policies while preserving valid actions.

## Why it stopped

No-paper closure: the result is a useful synthetic mechanism signal, not broad or publication-grade validation.

## Recommended next action

Run a bounded real-agent trace follow-up with LLM-generated tool calls, adversarial prompts, and independently produced evidence records before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent trace validation for local evidence-ledger policy verification
- Success threshold: At least 90% reduction in unsafe false allows versus execute-all baseline, valid false-reject rate under 5%, p95 verifier latency under 5 ms/action, and successful detection of all direct evidence-record mutations in a minimum 1,000-action labeled trace set.
- Stop condition: Stop if unsafe false allows remain above 10% of invalid labeled actions, valid false rejects exceed 5%, or evidence provenance cannot be separated from the action generator.

## Evidence references

- Artifact root: `<local-path>/projects/small-agent-evidence-ledger-with-local-policy-verifier-e1aa4e5ce2e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
