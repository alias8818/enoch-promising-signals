# Draft-Verify Ledger on Real LLM Tool-Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `draft-verify-ledger-on-real-llm-tool-agent-traces-1dfde503ad`
Run ID: `draft-verify-ledger-on-real-llm-tool-agent-traces-1dfde503ad-20260523T222413092588+0000`

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

- Parent run decision: Speculative Agent Verification via Draft-Verify Ledger: enoch://control-plane/projects/speculative-agent-verification-via-draft-verify-ledger-2191689b1909/runs/speculative-agent-verification-via-draft-verify-ledger-2191689b1909-20260523T215343991739+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b49cd735f64b

## What looked useful

On 25 real traces with 422 unique command entries and 2020 generated claims, ledger verification achieved 0 false positives and 0 false negatives, while naive corpus text matching had a 0.654 false-positive rate.

## Boundaries and scale limits

The test used local Codex command_execution traces and programmatically generated true/mutated claims. It did not evaluate free-form natural-language claim extraction, non-shell tool schemas, adversarial paraphrase, human labels, or a broad public trace corpus.

## Claim scope

A deterministic draft-verify ledger keyed to command-local evidence can reject controlled corrupted claims about command identity, exit code, and output-token evidence on 25 local real Codex tool-agent JSONL traces.

## Why it stopped

Mechanism supported in a bounded controlled direct test, but not paper-ready because claims were generated from event fields rather than extracted from natural-language agent outputs.

## Recommended next action

Deepen with a labeled natural-language claim extraction test: draft claims from real final answers or run notes, bind them to trace evidence, and verify at least 100 manually labeled claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-Language Drafted Ledger Claims on Real Agent Trace Summaries
- Success threshold: False-positive rate <= 0.10 and false-negative rate <= 0.15 on at least 100 manually labeled natural-language claims from real traces.
- Stop condition: Stop as negative if false-positive rate exceeds 0.25 or fewer than 60% of natural-language claims can be bound to concrete trace evidence without manual repair.

## Evidence references

- Artifact root: `<local-path>/projects/draft-verify-ledger-on-real-llm-tool-agent-traces-1dfde503ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
